import pandas as pd
from models import Policyholder, Claim

def load_data(filepath):
    df = pd.read_csv(filepath)
    df['CLAIM_DATE'] = pd.to_datetime(df['CLAIM_DATE'], errors='coerce')

    policyholders = {}
    claims = []

    for _, row in df.iterrows():
        cust_id = row['CUSTOMER_ID']
        if cust_id not in policyholders:
            policyholders[cust_id] = Policyholder(
                customer_id=cust_id,
                name=f"Customer {cust_id}",
                age=30,  # Placeholder
                policy_type="Health",  # Placeholder
                sum_insured=100000,  # Placeholder
                city=row.get('CITY', 'Unknown')
            )

        claim = Claim(
            claim_id=row['CLAIM_ID'],
            date=row['CLAIM_DATE'],
            amount=row['CLAIM_AMOUNT'],
            premium_collected=row['PREMIUM_COLLECTED'],
            paid_amount=row['PAID_AMOUNT'],
            rejection_remarks=row.get('REJECTION_REMARKS', '')
        )

        policyholders[cust_id].add_claim(claim)
        claims.append(claim)

    return policyholders, claims, df
