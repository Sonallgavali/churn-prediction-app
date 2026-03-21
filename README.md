Bank Churn Prediction 🚀
🧠 Project Overview

This project predicts whether a bank customer is likely to churn (leave the bank) using a Random Forest Classifier.

Before finalizing the model, several algorithms were compared:

Logistic Regression
Support Vector Machine (SVM)
Random Forest Classifier
K-Nearest Neighbors (KNN)

Random Forest was selected due to its highest accuracy, stability, and ability to handle feature interactions.

The model is trained on the full dataset and includes a preprocessing pipeline to handle numeric scaling and categorical encoding, ensuring accurate predictions for new customers.

The goal is to help banks identify at-risk customers and make data-driven decisions to improve retention.

⚙️ Tools & Technologies
Python 3.x
Jupyter Notebook
Libraries: pandas, scikit-learn, joblib
Machine Learning: Random Forest Classifier
Preprocessing: StandardScaler, OneHotEncoder, ColumnTransformer, Pipeline
🗂 Dataset

The dataset contains customer information such as:

Credit Score
Age
Tenure
Balance
Number of Products
Credit Card status
Active Member status
Estimated Salary
Geography
Gender

Target variable: Exited (1 = churned, 0 = stayed)

🚀 How It Works
1️⃣ Model Comparison
Multiple models were trained and evaluated: Logistic Regression, SVM, Random Forest, and KNN.
Random Forest was selected as the final model due to its superior performance on evaluation metrics.
2️⃣ Preprocessing
Numeric columns are scaled using StandardScaler.
Categorical columns are encoded using OneHotEncoder.
3️⃣ Final Model Training
Random Forest is trained on the full dataset within a pipeline, combining preprocessing and model training in a single step.
4️⃣ Prediction
The saved pipeline (churn_model_pipeline.pkl) can predict churn for any new customer, ensuring feature order and preprocessing are consistent.
📦 Project Structure
bank-churn-prediction/
│
├─ bank_churn_data.csv          # Original dataset
├─ churn_model_pipeline.pkl     # Saved Random Forest pipeline
├─ Churn_Prediction.ipynb       # Notebook with model comparison, training & pipeline
└─ README.md                    # Project documentation
💡 Example Usage
import pandas as pd
import joblib

# Load trained pipeline
pipeline = joblib.load("churn_model_pipeline.pkl")

# Example new customer data
new_customer = pd.DataFrame([{
    "CreditScore": 600,
    "Age": 40,
    "Tenure": 3,
    "Balance": 50000,
    "NumOfProducts": 2,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 50000,
    "Geography": "France",
    "Gender": "Male"
}])

# Predict churn
prediction = pipeline.predict(new_customer)
print("Churn Prediction:", prediction[0])
📌 Key Highlights
Comprehensive model comparison with Logistic Regression, SVM, KNN, and Random Forest.
End-to-end preprocessing pipeline ensures accurate predictions without manual intervention.
Trained on full dataset to maximize learning from all available data.
Deployment-ready, suitable for web apps, dashboards, or Streamlit projects.
🔗 Future Improvements
Hyperparameter tuning for better accuracy.
Handling class imbalance using SMOTE or weighted classes.
Integration with a real-time customer dashboard for predictions.
