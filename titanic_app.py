
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("best_model.joblib")

st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)

st.title("🚢 Titanic Survival Prediction")
st.write("Enter passenger details to predict survival.")

# Passenger inputs
col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("Passenger Class", [1, 2, 3])
    sex = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=0.0, max_value=100.0, value=25.0)
    sibsp = st.number_input("Siblings / Spouses", min_value=0, max_value=10, value=0)

with col2:
    parch = st.number_input("Parents / Children", min_value=0, max_value=10, value=0)
    fare = st.number_input("Ticket Fare", min_value=0.0, value=30.0)
    embarked = st.selectbox("Embarked Port", ["Southampton", "Queenstown", "Cherbourg"])

# Match the encoding used during model training
sex_value = 1 if sex == "Female" else 0

embarked_mapping = {
    "Southampton": 0,
    "Queenstown": 1,
    "Cherbourg": 2
}

embarked_value = embarked_mapping[embarked]

# Keep the exact training feature order
input_data = [[
    pclass,
    sex_value,
    age,
    sibsp,
    parch,
    fare,
    embarked_value
]]

# if st.button("Predict Survival"):
#     prediction = model.predict(input_data)[0]
#     probability = model.predict_proba(input_data)[0]

#     st.subheader("Prediction Result")

#     if prediction == 1:
#         st.success("The model predicts that the passenger survived.")
#     else:
#         st.error("The model predicts that the passenger did not survive.")

#     st.write(f"Predicted class: {prediction}")
#     st.write(f"Estimated survival probability: {probability[1] * 100:.2f}%")
#     st.write(f"Estimated non-survival probability: {probability[0] * 100:.2f}%")
