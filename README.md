# Business Churn Prediction

End-to-end customer churn prediction using machine learning and SHAP explainability.

## 🔍 Project Overview
Customer churn is a critical business problem where companies aim to identify customers who are likely to leave their services.

This project presents an end-to-end machine learning pipeline built on the Telco Customer Churn dataset, focusing on:
- Business-driven feature engineering
- Evaluation and selection of an interpretable baseline model
- Model explainability using SHAP
- Actionable business insights for retention

## 🔗 Project Links
- 📘 **Kaggle Notebook**: https://www.kaggle.com/code/abirhossain720/business-churn-prediction
- 💻 **GitHub Repository**: https://github.com/mdabir-hossain/business-churn-prediction

## 🧪 Dataset
- Telco Customer Churn dataset (IBM)
- ~7,000 customers
- Binary target: Churn (Yes / No)

## ⚙️ Modeling Approach
- Logistic Regression with a preprocessing pipeline
- One-hot encoding for categorical features
- Stratified train–test split
- Evaluation metric: ROC-AUC

**Final ROC-AUC:** ~0.83

## 🔍 Explainability
SHAP (SHapley Additive Explanations) was used to interpret model predictions and identify key churn drivers such as:
- Customer tenure
- Monthly and total charges
- Contract type (month-to-month vs long-term)
- Service count and CLTV

## 💡 Business Recommendations
1. Prioritise retention campaigns for new customers (< 12 months tenure).
2. Encourage month-to-month users to switch to long-term contracts.
3. Offer targeted discounts to high MonthlyCharges + Fiber optic customers.
4. Promote AutoPay and multi-service bundles.
5. Improve adoption of OnlineSecurity and TechSupport services.

## 🛠️ Tech Stack
Python, Pandas, NumPy, scikit-learn, SHAP, Matplotlib, Seaborn
