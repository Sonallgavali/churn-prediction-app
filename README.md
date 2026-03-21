🏦 Bank Customer Churn Prediction (End-to-End ML Project)

📌 Project Summary

Customer churn is a critical problem in the banking sector, as losing customers directly affects revenue and growth.

In this project, I built a complete end-to-end Machine Learning pipeline to predict whether a customer is likely to leave the bank. The project focuses not just on model building, but also on business understanding, model comparison, and actionable insights.

---

🎯 Business Objective

- Identify customers who are likely to churn
- Help the bank take proactive retention actions
- Minimize revenue loss by targeting high-risk customers

---

📂 Dataset Overview

The dataset contains customer-level information such as demographics, account details, and activity status.

🔑 Key Features:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Active Member Status
- Estimated Salary

🎯 Target Variable:

- "Exited" → 1 (Churn), 0 (No Churn)

🧹 Data Cleaning:

- Removed irrelevant columns: "CustomerId", "Surname"
- No major missing values observed

---

⚙️ Approach & Methodology

1️⃣ Data Preprocessing

- Performed train-test split (80-20)
- Applied One-Hot Encoding for categorical variables ("Geography", "Gender")
- Applied Feature Scaling (for KNN, SVM, Logistic Regression)
- Checked for class imbalance in churn data

---

2️⃣ Model Building

I implemented and compared multiple machine learning models:

- Logistic Regression (Baseline)
- Decision Tree Classifier
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Random Forest Classifier ✅

---

3️⃣ Model Evaluation

Since churn prediction is an imbalanced classification problem, I used multiple evaluation metrics:

- Accuracy Score
- Confusion Matrix
- Precision
- Recall (Primary Focus)
- F1-Score
- ROC-AUC Score

📌 Why Recall?
Because missing a churn customer means potential business loss.

---

🏆 Final Model Selection

After comparing all models,
👉 Random Forest Classifier was selected as the final model

🔍 Why Random Forest?

- Captures non-linear relationships effectively
- Reduces overfitting compared to Decision Trees
- Works well with mixed feature types
- Provided the best balance of Recall and Accuracy

---

📊 Results & Performance

- Achieved strong overall performance (~80–85% accuracy)
- Improved detection of churn customers compared to baseline
- Random Forest outperformed other models in Recall and ROC-AUC

---

📈 Key Insights (Business Value)

- 🔴 Customers who are not active members are more likely to churn
- 🔴 Customers with fewer products tend to leave the bank
- 🔴 Older customers show higher churn probability
- 🔴 Certain geographies have higher churn rates
- 🔴 Low engagement is a strong indicator of churn

📌 These insights can help the bank:

- Design targeted retention campaigns
- Improve customer engagement strategies
- Reduce churn and increase profitability

---

🛠️ Tech Stack

- Python 🐍
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn

---

🚀 How to Run the Project

1. Clone the repository:

git clone https://github.com/your-username/bank-churn-prediction.git

2. Install dependencies:

pip install -r requirements.txt

3. Run the notebook:

jupyter notebook

---

📌 Project Highlights (For Recruiters)

- End-to-end ML pipeline implementation
- Strong understanding of model evaluation beyond accuracy
- Focus on business-driven metrics (Recall)
- Comparison of multiple ML models
- Extraction of actionable business insights

---

🔮 Future Improvements

- Hyperparameter tuning (GridSearchCV / RandomizedSearchCV)
- Handling imbalance using SMOTE
- Integration with Power BI dashboard for business reporting

---

📧 Contact

Feel free to connect for discussion or collaboration!

---
