#  Insurance Claims Data Preprocessing & City Analysis

This Python script (`clean.py`) automates the process of cleaning and analyzing insurance claims data without using external libraries like `pandas` or `numpy`. It handles missing and invalid values, classifies rejection remarks, and recommends a city for operational shutdown based on financial loss ratios.

##  Features

*  **CSV File Preprocessing**: Cleans missing/null/invalid values.

*  **Rejection Remarks Classification**: Classifies rejections as:

  * `Fake_document`

  * `Not_Covered`

  * `Policy_expired`

  * `Unknown`

  * `No Remark`

*  **City Shutdown Recommendation**: Calculates the claim-to-premium loss ratio for four cities and suggests which one to shut down.

##  File Structure


assignment--2/
│
├── assignment2.py    # Main Python script
├── README.md # This file



##  How to Run

1. Clone the repository and navigate into the project folder:


git clone https://github.com/your-username/your-repo.git
cd your-repo/insurance_analysis


Ensure your `Insurance_auto_data.csv` file is placed inside the folder.

2. Run the script using Python 3:


python3 clean.py


##  Sample Output


--- City Analysis ---

Pune: Claims = ₹104190.00, Premiums = ₹2198.59, Loss Ratio = 47.38
Kolkata: Claims = ₹68000.00, Premiums = ₹13400.00, Loss Ratio = 5.07
Ranchi: Claims = ₹50000.00, Premiums = ₹10000.00, Loss Ratio = 5.00
Guwahati: Claims = ₹98365.00, Premiums = ₹10844.00, Loss Ratio = 9.07

Suggested city to shut down based on highest loss ratio: **Kolkata**

--- Sample Cleaned Data ---
{'CLAIM_ID': 'CLM100021', 'CLAIM_DATE': '2025-04-01', 'CUSTOMER_ID': 'CUST14285', 'CLAIM_AMOUNT': 10419.0, 'PREMIUM_COLLECTED': 2198.59, 'PAID_AMOUNT': 6964.46, 'CITY': 'PUNE', 'REJECTION_REMARKS': None, 'REJECTION_CLASS': 'No Remark'}
{'CLAIM_ID': 'CLM100013', 'CLAIM_DATE': '2025-04-01', 'CUSTOMER_ID': 'CUST26471', 'CLAIM_AMOUNT': 42468.0, 'PREMIUM_COLLECTED': 8982.2, 'PAID_AMOUNT': 30119.67, 'CITY': 'GUWAHATI', 'REJECTION_REMARKS': None, 'REJECTION_CLASS': 'No Remark'}
{'CLAIM_ID': 'CLM100099', 'CLAIM_DATE': '2025-04-02', 'CUSTOMER_ID': 'CUST29309', 'CLAIM_AMOUNT': 55897.0, 'PREMIUM_COLLECTED': 1861.78, 'PAID_AMOUNT': 55657.15, 'CITY': 'GUWAHATI', 'REJECTION_REMARKS': None, 'REJECTION_CLASS': 'No Remark'}
{'CLAIM_ID': 'CLM100044', 'CLAIM_DATE': '2025-04-02', 'CUSTOMER_ID': 'CUST30275', 'CLAIM_AMOUNT': 71785.0, 'PREMIUM_COLLECTED': 13154.99, 'PAID_AMOUNT': 53629.3, 'CITY': 'PUNE', 'REJECTION_REMARKS': None, 'REJECTION_CLASS': 'No Remark'}



## Limitations

* No external libraries used (per constraints).

* Assumes CSV fields are comma-separated and cleanly formatted.




