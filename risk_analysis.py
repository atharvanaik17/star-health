from datetime import datetime
import pandas as pd

def identify_high_risk(policyholders):
    high_risk_list = []
    today = datetime.today()

    for ph in policyholders.values():
        total_claim_amount = ph.total_claim_amount()
        claim_frequency = ph.claim_frequency_last_year(today)

        if claim_frequency > 3 or (total_claim_amount > 0.8 * ph.sum_insured):
            high_risk_list.append({
                "Customer ID": ph.customer_id,
                "Name": ph.name,
                "City": ph.city,
                "Claims in Last Year": claim_frequency,
                "Total Claim Amount": total_claim_amount,
                "Sum Insured": ph.sum_insured,
                "Claim Ratio": round(total_claim_amount / ph.sum_insured, 2)
            })

    return high_risk_list
def calculate_claim_frequency(policyholders):
    freq = []
    for ph in policyholders.values():
        freq.append({
            'Customer ID': ph.customer_id,
            'Claim Frequency': len(ph.claims)
        })
    return pd.DataFrame(freq)


