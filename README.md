# Credit-Risk-Modelling
Overview

This project is a Credit Risk Prediction Web Application built using Streamlit, Machine Learning, and Financial Analytics. The application helps assess whether a loan applicant is likely to be a Good Credit Risk or Bad Credit Risk based on their financial and personal information.

The project is based on the German Credit Dataset and demonstrates an end-to-end workflow including data preprocessing, model building, and deployment.

Objective

The goal of this project is to:

Predict the creditworthiness of loan applicants

Support data-driven lending decisions

Demonstrate practical implementation of credit risk modeling

Build a deployable analytics solution for real-world financial applications

Features

User-friendly web interface using Streamlit

Real-time credit risk prediction

Pre-trained Machine Learning model (XGBoost)

Encoded categorical features using saved encoders

Instant classification:

Good Credit Risk

Bad Credit Risk

Tech Stack

Python

Streamlit

Pandas & NumPy

Scikit-learn

XGBoost

Joblib

Project Structure
credit-risk-app/
│
├── app.py                         # Streamlit application
├── xgb_model.pkl                  # Trained XGBoost model
├── Checking_account_encoder.pkl
├── Saving_accounts_encoder.pkl
├── Housing_encoder.pkl
├── Sex_encoder.pkl
├── target_encoder.pkl
├── german_credit_data.csv         # Dataset (if used)
├── requirements.txt               # Dependencies
└── README.md
Model Details

Algorithm: XGBoost Classifier

Problem Type: Binary Classification

Target: Credit Risk (Good / Bad)

Feature Engineering:

Label Encoding for categorical variables

Saved encoders for consistent predictions

How to Run Locally
Step 1: Clone the repository
git clone https://github.com/your-username/credit-risk-app.git
cd credit-risk-app
Step 2: Install dependencies
pip install -r requirements.txt
Step 3: Run the app
streamlit run app.py

The app will open in your browser.

Live Deployment

The application is deployed using Streamlit Community Cloud.

(Replace with your link after deployment)

Business Use Case

This type of model can be used by:

Banks and NBFCs for loan screening

Fintech companies for automated risk assessment

Credit analysts for decision support

It helps reduce default risk and improve lending efficiency.

Future Improvements

Add probability score and risk categories

Integrate Power BI dashboard

Add model explainability (SHAP)

Connect to a database for real-time applications

Author

Rohan Kumar
PGDM – Finance & Analytics

License

This project is for academic and learning purposes.
