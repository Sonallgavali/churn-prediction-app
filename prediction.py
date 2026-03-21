import streamlit as st
import pandas as pd
import pickle

def run():

    st.title("🔮 Customer Churn Prediction")

    # ---------------- LOAD MODEL ----------------
    model = pickle.load(open("model/churn_model.pkl", "rb"))
    columns = pickle.load(open("model/model_columns.pkl", "rb"))

    # ---------------- USER INPUT ----------------
    credit_score = st.number_input("Credit Score", 300, 900, 600)
    age = st.slider("Age", 18, 92, 35)
    tenure = st.slider("Tenure (Years)", 0, 10, 3)
    balance = st.number_input("Balance", 0.0, 250000.0, 50000.0)
    num_products = st.slider("Number of Products", 1, 4, 1)
    has_card = st.selectbox("Has Credit Card", [0, 1])
    is_active = st.selectbox("Is Active Member", [0, 1])
    salary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)

    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Male", "Female"])

    # ---------------- CREATE INPUT DATA ----------------
    input_dict = {
        "CreditScore": credit_score,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": num_products,
        "HasCrCard": has_card,
        "IsActiveMember": is_active,
        "EstimatedSalary": salary
    }

    input_df = pd.DataFrame([input_dict])

    # ---------------- ONE HOT ENCODING ----------------
    input_df["Geography_Germany"] = 1 if geography == "Germany" else 0
    input_df["Geography_Spain"] = 1 if geography == "Spain" else 0
    input_df["Gender_Male"] = 1 if gender == "Male" else 0

    # ---------------- ALIGN WITH TRAINING COLUMNS ----------------
    input_df = input_df.reindex(columns=columns, fill_value=0)

    st.write("### 🔍 Input Data")
    st.dataframe(input_df)

    # ---------------- PREDICTION ----------------
    if st.button("Predict"):

        pred = model.predict(input_df)[0]

        # 👉 Correct probability (churn = class 1)
        prob_churn = model.predict_proba(input_df)[0][1]

        # ---------------- OUTPUT ----------------
        if pred == 1:
            st.error(f"🚨 Customer will CHURN | Probability: {prob_churn:.2%}")
        else:
            st.success(f"✅ Customer will STAY | Probability: {(1 - prob_churn):.2%}")

        # ---------------- RISK LEVEL ----------------
        st.subheader("⚠️ Risk Level")

        if prob_churn > 0.7:
            st.error("High Risk 🔴")
        elif prob_churn > 0.4:
            st.warning("Medium Risk 🟠")
        else:
            st.success("Low Risk 🟢")