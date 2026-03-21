import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

def run():

    st.title("📊 Customer Segmentation Dashboard")

    # -----------------------------
    # LOAD DATA & MODEL
    # -----------------------------

    df = pd.read_csv("data/Bank_Churn.csv")
    model = joblib.load("model/churn_model.pkl")

    columns_to_drop = ["RowNumber", "CustomerId", "Surname"]
    df = df.drop(columns=columns_to_drop, errors="ignore")
    df = pd.get_dummies(df, drop_first=True)

    # -----------------------------
    # RISK SEGMENTATION
    # -----------------------------
    st.subheader("🎯 Risk-Based Segmentation")

    X = df.drop("Exited", axis=1)
    df["churn_prob"] = model.predict_proba(X)[:, 1]

    def segment_risk(p):
        if p > 0.7:
            return "High Risk 🔴"
        elif p > 0.4:
            return "Medium Risk 🟠"
        else:
            return "Low Risk 🟢"

    df["Risk Segment"] = df["churn_prob"].apply(segment_risk)

    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots()
        sns.countplot(x="Risk Segment", data=df, ax=ax)
        ax.set_title("Customer Risk Segmentation")
        st.pyplot(fig)

    with col2:
        st.write("### 📌 Insights")
        st.write(df["Risk Segment"].value_counts())

    # -----------------------------
    # BUSINESS SEGMENTATION
    # -----------------------------
    st.subheader("💼 Business Segmentation")

    def business_segment(row):
        if row["Balance"] > 100000 and row["IsActiveMember"] == 1:
            return "Premium 💎"
        elif row["IsActiveMember"] == 0 and row["Balance"] > 50000:
            return "At Risk ⚠️"
        elif row["Balance"] < 50000:
            return "Low Value 📉"
        else:
            return "Loyal 🟢"

    df["Business Segment"] = df.apply(business_segment, axis=1)

    col3, col4 = st.columns(2)

    with col3:
        fig2, ax2 = plt.subplots()
        sns.countplot(x="Business Segment", data=df, ax=ax2)
        ax2.set_title("Business Segments")
        plt.xticks(rotation=20)
        st.pyplot(fig2)

    with col4:
        st.write("### 📌 Insights")
        st.write(df["Business Segment"].value_counts())

    # -----------------------------
    # FILTER
    # -----------------------------
    st.subheader("🔍 Filter Customers")

    segment_filter = st.selectbox(
        "Select Risk Segment",
        ["All", "High Risk 🔴", "Medium Risk 🟠", "Low Risk 🟢"]
    )

    if segment_filter != "All":
        filtered_df = df[df["Risk Segment"] == segment_filter]
    else:
        filtered_df = df

    st.dataframe(filtered_df.head(50))