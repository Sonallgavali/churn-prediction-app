import streamlit as st
import pandas as pd
import pickle

def run():

    st.title("⚠️ Customer Risk Ranking")

    model = pickle.load(open("model/churn_model.pkl", "rb"))
    columns = pickle.load(open("model/model_columns.pkl", "rb"))

    df = pd.read_csv("data/bank_churn.csv")

    df_model = pd.get_dummies(df, drop_first=True)
    df_model = df_model.reindex(columns=columns, fill_value=0)

    df['Churn_Probability'] = model.predict_proba(df_model)[:,1]

    top_risk = df.sort_values(by='Churn_Probability', ascending=False).head(10)

    st.dataframe(top_risk[['CustomerId','Age','Balance','Churn_Probability']])