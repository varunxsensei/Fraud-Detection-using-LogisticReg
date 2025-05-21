import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud detection Prediction App")

st.markdown("Please enter transaction details and use prediction button")

st.divider()

transaction_type = st.selectbox("Transaction Type",["PAYMENT","CASH_OUT","DEPOSIT","TRANSFER"])

amount = st.number_input("Amount",min_value = 0.0,value = 1000.0)

oldbalanceOrig = st.number_input("Old balance (sender)",min_value = 0.0,value = 10000.0)
newbalanceOrig = st.number_input("New balance (sender)",min_value = 0.0,value = 9000.0)
oldbalanceDest = st.number_input("Old balance (receiver)",min_value = 0.0,value = 0.0)
newbalanceDest = st.number_input("New balance (receiver)",min_value = 0.0,value = 0.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount":amount,
        "oldbalanceOrg" : oldbalanceOrig,
        "newbalanceOrig":newbalanceOrig,
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest":newbalanceDest
    }])

    prediction = model.predict(input_data)[0]
    
    st.subheader(f"Prediction : {int(prediction)}")

    if prediction == 1:
        st.error("This transaction can be fraud")

    else:
        st.success("This transaction looks like its not a fraud")    