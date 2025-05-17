import streamlit as st
import pandas as pd
import os
from datetime import datetime
from data_loader import load_data
from risk_analysis import identify_high_risk, calculate_claim_frequency
from reports import claims_dataframe, monthly_claims, average_claim_by_city, highest_claim
from models import Policyholder, Claim

DATA_FILE = 'Insurance_auto_data.csv'


if 'policyholders' not in st.session_state or 'claims' not in st.session_state:
    policyholders, claims, df_raw = load_data(DATA_FILE)
    st.session_state.policyholders = policyholders
    st.session_state.claims = claims
else:
    policyholders = st.session_state.policyholders
    claims = st.session_state.claims


def append_claim_to_csv(claim, customer_id, city):
    new_entry = {
        "CLAIM_ID": claim.claim_id,
        "CLAIM_DATE": claim.date.strftime("%Y-%m-%d"),
        "CUSTOMER_ID": customer_id,
        "CLAIM_AMOUNT": claim.claim_amount,
        "PREMIUM_COLLECTED": claim.premium_collected,
        "PAID_AMOUNT": claim.paid_amount,
        "CITY": city,
        "REJECTION_REMARKS": claim.rejection_remarks
    }
    df = pd.DataFrame([new_entry])
    df.to_csv(DATA_FILE, mode='a', header=not os.path.exists(DATA_FILE), index=False)


st.set_page_config(page_title="Insurance System", layout="wide")
st.title(" Insurance Claim Management System")

menu = ["Home", "Policyholders", "Claims", "Risk Analysis", "Reports"]
choice = st.sidebar.selectbox("Select Module", menu)


if choice == "Home":
    st.write("Welcome to the Insurance Claim Management System")
    st.write("Use the menu on the left to navigate between modules.")


elif choice == "Policyholders":
    st.header("Policyholder Management")

    st.subheader("List of Policyholders")
    ph_data = []
    for ph in policyholders.values():
        ph_data.append({
            "Customer ID": ph.customer_id,
            "Name": ph.name,
            "Age": ph.age,
            "Policy Type": ph.policy_type,
            "Sum Insured": ph.sum_insured,
            "City": ph.city,
            "Total Claims": len(ph.claims)
        })
    st.dataframe(pd.DataFrame(ph_data))

    st.subheader("Register New Policyholder")
    with st.form("policyholder_form", clear_on_submit=True):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=18, max_value=100, step=1)
        policy_type = st.selectbox("Policy Type", ["Health", "Vehicle", "Life"])
        sum_insured = st.number_input("Sum Insured", min_value=10000, step=1000)
        city = st.text_input("City")
        submitted = st.form_submit_button("Register Policyholder")

        if submitted:
            new_id = f"CUST{10000 + len(policyholders) + 1}"
            new_ph = Policyholder(new_id, name, age, policy_type, sum_insured, city)
            policyholders[new_id] = new_ph
            st.session_state.policyholders = policyholders 
            st.success(f"Policyholder {name} registered with ID {new_id}")
            st.info("Note: Data will be persisted only after a claim is submitted.")


elif choice == "Claims":
    st.header("Claim Management")

    st.subheader("Add New Claim")

    if policyholders:  
        with st.form("claim_form", clear_on_submit=True):
            claim_id = st.text_input("Claim ID")
            customer_id = st.selectbox("Policyholder ID", list(policyholders.keys()))
            claim_amount = st.number_input("Claim Amount", min_value=0.0, step=100.0)
            premium_collected = st.number_input("Premium Collected", min_value=0.0, step=100.0)
            paid_amount = st.number_input("Paid Amount", min_value=0.0, step=100.0)
            rejection_remarks = st.text_input("Rejection Remarks (leave blank if approved)")
            date = st.date_input("Date of Claim", value=datetime.today())
            submit_claim = st.form_submit_button("Submit Claim")

            if submit_claim:
                claim = Claim(claim_id, date, claim_amount, premium_collected, paid_amount, rejection_remarks)
                policyholders[customer_id].add_claim(claim)
                claims.append(claim)
                city = policyholders[customer_id].city
                append_claim_to_csv(claim, customer_id, city)
                st.session_state.claims = claims  
                st.session_state.policyholders = policyholders
                st.success(f"Claim {claim_id} added for customer {customer_id} and saved.")
    else:
        st.warning("No policyholders found. Please register one first.")

    st.subheader("All Claims")
    claims_data = []
    for claim in claims:
        claims_data.append({
            "Claim ID": claim.claim_id,
            "Date": claim.date.strftime("%Y-%m-%d"),
            "Claim Amount": claim.claim_amount,
            "Premium Collected": claim.premium_collected,
            "Paid Amount": claim.paid_amount,
            "Rejection Remarks": claim.rejection_remarks
        })
    st.dataframe(pd.DataFrame(claims_data))


elif choice == "Risk Analysis":
    st.header(" Risk Analysis")

    st.write("### Claim Frequency per Policyholder")
    freq_df = calculate_claim_frequency(policyholders)
    st.dataframe(freq_df)

    st.write("### High Risk Policyholders")
    high_risk = identify_high_risk(policyholders)
    st.dataframe(high_risk)


elif choice == "Reports":
    st.header(" Reports")

    st.subheader("All Claims Data")
    st.dataframe(claims_dataframe(policyholders))

    st.subheader(" Date vs Claim Count")
    monthly_df = monthly_claims(claims)
    if not monthly_df.empty:
        monthly_df['Month'] = monthly_df['Month'].astype(str)
        st.bar_chart(data=monthly_df.set_index('Month')['Total Claims'])
    else:
        st.warning("No monthly claim data available.")

    st.subheader("Average Claim Amount by City")
    avg_city_df = average_claim_by_city(policyholders)
    st.dataframe(avg_city_df)

    st.subheader(" Highest Claim Details")
    highest = highest_claim(claims)
    if highest is not None:
        st.write(highest)
    else:
        st.warning("No valid claim data available.")
