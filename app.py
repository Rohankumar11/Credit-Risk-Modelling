#1 Good(lower risk) 0 Bad(higher risk) 
import streamlit as st 
import pandas as pd
import joblib


model=joblib.load("xgb_model.pkl")
#encoders={col:joblib.load(f"{col}_encoder.pkl") for col in ['Sex','Housing','Saving accounts','Checking accounts']}
encoders = {
    "Sex": joblib.load("Sex_encoder.pkl"),
    "Housing": joblib.load("Housing_encoder.pkl"),
    "Saving accounts": joblib.load("Saving_accounts_encoder.pkl"),
    "Checking accounts": joblib.load("Checking_account_encoder.pkl")
}
st.title("Credit Risk Prediction")
st.write("Enter the details to predict credit risk")    

age=st.number_input("Age",min_value=18,max_value=80,value=30)
sex = st.selectbox(
    "Sex",
    options=[0, 1],
    format_func=lambda x: "male" if x == 1 else "female"
)
job=st.number_input("Job (0-3)",min_value=0,max_value=3,value=1)
housing=st.selectbox("Housing",["own","rent","free"])
saving_accounts=st.selectbox("Saving Accounts",["little","moderate","rich","quite rich"])
checking_accounts=st.selectbox("Checking Accounts",["little","moderate","rich"])
credit_amount=st.number_input("Credit Amount",min_value=0,value=1000)

duration=st.number_input("Duration (in months)",min_value=1,max_value=12)
input_df = pd.DataFrame({
    'Age': [age],
    'Sex': [sex],  # already numeric
    'Job': [job],
    'Housing': [encoders['Housing'].transform([housing])[0]],
    'Saving accounts': [encoders['Saving accounts'].transform([saving_accounts])[0]],
    'Checking account': [encoders['Checking accounts'].transform([checking_accounts])[0]],
    'Credit amount': [credit_amount],
    'Duration': [duration]
})
if st.button("Predict Risk"):   
    prediction=model.predict(input_df)
    if prediction[0]==1:
        st.success("The predicted credit risk is: **Good**")
    else:
        st.error("The predicted credit risk is: **Bad**")