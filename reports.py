import pandas as pd
from datetime import datetime

def claims_dataframe(policyholders):
    all_claims = []

    for ph in policyholders.values():
        for claim in ph.claims:
            all_claims.append({
                "Claim ID": claim.claim_id,
                "Customer ID": ph.customer_id,
                "Name": ph.name,
                "Claim Amount": claim.claim_amount,
                "Status": claim.status,
             
                "Date": claim.date.strftime("%Y-%m-%d"),
                "City": ph.city,
                "Policy Type": ph.policy_type
            })

    return pd.DataFrame(all_claims)

def monthly_claims(data):
    
    
    if isinstance(data, pd.DataFrame):
        df = data.copy()
    else:
        df = pd.DataFrame([{
            "Date": claim.date,
            "Amount": getattr(claim, 'claim_amount', None)
        } for claim in data])
    
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')  # coerce invalid dates to NaT
    df = df.dropna(subset=["Date"])  # remove rows with invalid dates

    if df.empty:
        return pd.DataFrame(columns=["Month", "Total Claims"])

    df["Month"] = df["Date"].dt.to_period("D")
    return df.groupby("Month").size().reset_index(name="Total Claims")

def average_claim_by_city(policyholders):
    

    data = []
    for ph in policyholders.values():
        for claim in ph.claims:
            data.append({
                "City": ph.city,
                "Claim Amount": claim.claim_amount
            })

    df = pd.DataFrame(data)
    df = df.dropna(subset=["City", "Claim Amount"])

    return df.groupby("City")["Claim Amount"].mean().reset_index(name="Average Claim Amount")


def highest_claim(claims):
    if not claims:
        return None

    # Convert the list of Claim objects to a DataFrame
    df = pd.DataFrame([{
        "Claim ID": c.claim_id,
        "Date": c.date,
        "Claim Amount": c.claim_amount,
        "Paid Amount": c.paid_amount,
        "Premium Collected": c.premium_collected,
        "Rejection Remarks": c.rejection_remarks,
    } for c in claims])

    # Ensure 'Claim Amount' exists and is numeric
    df["Claim Amount"] = pd.to_numeric(df["Claim Amount"], errors="coerce")

    if df["Claim Amount"].isnull().all():
        return None

    max_row = df.loc[df["Claim Amount"].idxmax()]
    return max_row