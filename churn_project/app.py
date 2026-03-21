import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Bank Churn App",
    page_icon="🏦",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("🏦 Bank Customer Analytics Platform")

# ---------------- NAVIGATION ----------------
menu = st.sidebar.radio(
    "📌 Navigation",
    ["Dashboard", "Churn Prediction", "Customer Segmentation", "Risk Ranking", "Project Info"]
)

# ---------------- ROUTING ----------------
if menu == "Dashboard":
    from dashboard import run
    run()

elif menu == "Churn Prediction":
    from prediction import run
    run()

elif menu == "Customer Segmentation":
    from segmentation import run
    run()

elif menu == "Risk Ranking":
    from risk_ranking import run
    run()

elif menu == "Project Info":
    from project_info import run
    run()