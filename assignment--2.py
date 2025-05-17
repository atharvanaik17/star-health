import csv


REJECTION_REASONS_MAP = {
    "fake_document": "Fake_document",
    "not_covered": "Not_Covered",
    "policy_expired": "Policy_expired"
}

def handle_error(error_message):
    print(f"Error: {error_message}")
    return "Error"

def contains_rejection_reason(rejection_text, reason):
    try:
        if rejection_text and isinstance(rejection_text, str):
            return reason.lower().replace("_", " ") in rejection_text.lower().replace("_", " ")
    except Exception as e:
        handle_error(f"Error in contains_rejection_reason: {str(e)}")
        return False
    return False

def map_rejection_reason(rejection_text):
    try:
        if rejection_text and isinstance(rejection_text, str):
            for reason, rejection_class in REJECTION_REASONS_MAP.items():
                if contains_rejection_reason(rejection_text, reason):
                    return rejection_class
            return "Unknown"
        else:
            return "No Remark"
    except Exception as e:
        handle_error(f"Error in map_rejection_reason: {str(e)}")
        return "Error"

def complex_rejection_classifier(remark_text):
    try:
        if not isinstance(remark_text, str) or len(remark_text.strip()) == 0:
            return "No Remark"

        fake_doc = contains_rejection_reason(remark_text, "fake_document")
        not_covered = contains_rejection_reason(remark_text, "not_covered")
        policy_expired = contains_rejection_reason(remark_text, "policy_expired")

        if fake_doc:
            return "Fake_document"
        elif not_covered:
            return "Not_Covered"
        elif policy_expired:
            return "Policy_expired"
        else:
            return map_rejection_reason(remark_text)
    except Exception as e:
        handle_error(f"Error in complex_rejection_classifier: {str(e)}")
        return "Error"

def preprocess_and_analyze(csv_file_path):
    cleaned_data = []
    cities_to_check = ["pune", "kolkata", "ranchi", "guwahati"]
    city_stats = {}

    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cleaned_row = {}

                for key, val in row.items():
                    val = val.strip() if val else None
                    if val is None or val.lower() in ['null', 'na', 'none']:
                        cleaned_row[key] = None
                    else:
                        try:
                            if key in ['CLAIM_AMOUNT', 'PREMIUM_COLLECTED', 'PAID_AMOUNT']:
                                cleaned_row[key] = float(val)
                            else:
                                cleaned_row[key] = val
                        except:
                            cleaned_row[key] = val

                
                remark = cleaned_row.get('REJECTION_REMARKS')
                cleaned_row['REJECTION_CLASS'] = complex_rejection_classifier(remark)
                cleaned_data.append(cleaned_row)

                
                city = cleaned_row.get('CITY')
                if city:
                    city_lower = city.strip().lower()
                    if city_lower in cities_to_check:
                        claim = cleaned_row.get('CLAIM_AMOUNT') or 0.0
                        premium = cleaned_row.get('PREMIUM_COLLECTED') or 0.0
                        if city_lower not in city_stats:
                            city_stats[city_lower] = {'claims': 0.0, 'premiums': 0.0}
                        city_stats[city_lower]['claims'] += float(claim)
                        city_stats[city_lower]['premiums'] += float(premium)

        
        print("\n--- City Analysis ---")
        worst_city = None
        worst_ratio = -1
        for city, stats in city_stats.items():
            claims = stats['claims']
            premiums = stats['premiums']
            ratio = (claims / premiums) if premiums > 0 else float('inf')
            print(f"{city.capitalize()}: Claims = ₹{claims:.2f}, Premiums = ₹{premiums:.2f}, Loss Ratio = {ratio:.2f}")

            if ratio > worst_ratio:
                worst_ratio = ratio
                worst_city = city

        if worst_city:
            print(f"\n🔍 Suggested city to shut down based on highest loss ratio: **{worst_city.capitalize()}**")
        else:
            print("\n🔍 No matching city found in the data.")

    except Exception as e:
        handle_error(f"Failed to process file: {str(e)}")

    return cleaned_data

if __name__ == "__main__":
    file_path = '/Users/atharva/Desktop/assignment--2/Insurance_auto_data.csv'
    cleaned_output = preprocess_and_analyze(file_path)

    print("\n--- Sample Cleaned Data ---")
    for row in cleaned_output[:100]:
        print(row)
