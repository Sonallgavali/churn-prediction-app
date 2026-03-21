import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run():

    st.title("📊 Customer Churn Dashboard")

    df = pd.read_csv("data/bank_churn.csv")

    # ---------------- KPIs ----------------
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Customers", len(df))
    col2.metric("Churn Rate", f"{df['Exited'].mean()*100:.2f}%")
    col3.metric("Avg Balance", f"{df['Balance'].mean():,.0f}")

    st.write("---")

    # ---------------- CHART 1 ----------------
    st.subheader("📉 Churn Distribution")

    fig, ax = plt.subplots()
    sns.countplot(x='Exited', data=df, ax=ax)
    ax.set_title("Customer Churn Count (0 = Stay, 1 = Churn)")
    ax.set_xlabel("Churn Status")
    ax.set_ylabel("Number of Customers")

    st.pyplot(fig)

    # ---------------- CHART 2 ----------------
    st.subheader("🌍 Churn by Geography")

    fig, ax = plt.subplots()
    sns.countplot(x='Geography', hue='Exited', data=df, ax=ax)
    ax.set_title("Churn Distribution Across Countries")
    ax.set_xlabel("Geography")
    ax.set_ylabel("Customer Count")

    st.pyplot(fig)

    # ---------------- CHART 3 ----------------
    st.subheader("👤 Age vs Churn")

    fig, ax = plt.subplots()
    sns.boxplot(x='Exited', y='Age', data=df, ax=ax)
    ax.set_title("Age Distribution by Churn Status")
    ax.set_xlabel("Churn Status")
    ax.set_ylabel("Age")

    st.pyplot(fig)

    # ---------------- CHART 4 ----------------
    st.subheader("💰 Balance vs Churn")

    fig, ax = plt.subplots()
    sns.boxplot(x='Exited', y='Balance', data=df, ax=ax)
    ax.set_title("Balance Distribution by Churn Status")
    ax.set_xlabel("Churn Status")
    ax.set_ylabel("Account Balance")

    st.pyplot(fig)

    # ---------------- KEY INSIGHTS ----------------
    st.write("---")
    st.subheader("💡 Key Business Insights")

    churn_rate = df['Exited'].mean()*100

    st.markdown(f"""
    - 📊 Overall churn rate is **{churn_rate:.2f}%**
    - 👤 Older customers show **higher churn tendency**
    - 🌍 Certain regions (e.g., Germany) show **higher churn rates**
    - 💰 Customers with **higher balances are more likely to churn**
    - ⚡ Inactive customers are at **high risk of leaving**
    """)

    # ---------------- RECOMMENDATIONS ----------------
    st.subheader("🚀 Recommendations")

    st.markdown("""
    - 🎯 Target inactive users with engagement campaigns  
    - 💳 Offer personalized plans for high-balance customers  
    - 🌍 Focus retention strategies in high-churn regions  
    - 📈 Promote cross-selling to increase product usage  
    """)