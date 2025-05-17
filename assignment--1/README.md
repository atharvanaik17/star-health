# Insurance Claim Management System

An interactive web application built with **Streamlit** to manage insurance policyholders and claims data, analyze risk, and generate reports.

---

## Features

- **Register and manage policyholders**
- **View and manage insurance claims**
- **Risk analysis** including claim frequency and identifying high-risk policyholders
- **Generate reports** and visualize claim data trends

---

## Technologies Used

- **Python**
- **Streamlit** (UI framework)
- **Pandas** (data manipulation)
- **CSV files** for data storage

---

## Setup Instructions

1.  **Clone the repository**

    ```bash
    git clone [https://github.com/atharvanaik17/star-health.git](https://github.com/atharvanaik17/star-health.git)
    cd star-health
    ```

2.  **Create and activate a virtual environment (recommended)**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install required packages**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app**

    ```bash
    streamlit run app.py
    ```

---

## Usage Guide

Use the sidebar menu to navigate between modules:

-   **Home**: Welcome page with basic information.
-   **Policyholders**: View the list of registered policyholders.
-   **Claims**: View claims data and add new claims.
-   **Risk Analysis**: Analyze claim frequency and identify high-risk policyholders.
-   **Reports**: View summarized claim reports and charts for insights.

To register or update policyholders or claims, follow the instructions provided in the UI modules.

---

## Project Structure

```bash


├── assignment--1/            # Assignment files and code
│
├── app.py                    # Main Streamlit application
├── data_loader.py            # Data loading and saving utilities
├── risk_analysis.py          # Risk analysis functions
├── reports.py                # Reporting functions
├── requirements.txt          # Python dependencies
├── Insurance_auto_data.csv   # Sample insurance data
└── README.md                 # This file
