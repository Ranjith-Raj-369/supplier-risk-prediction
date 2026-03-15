import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(page_title="Supplier Risk AI", page_icon="📦", layout="wide")

# Load model
model = joblib.load("supplier_risk_model.pkl")

# Title
st.title("📦 AI Supplier Risk Prediction Dashboard")
st.markdown("""
This AI tool predicts the **risk level of suppliers** based on operational and financial indicators.
Supply chain managers can use this system to identify high-risk suppliers early.
""")

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    year = st.slider("Year", 2018, 2030, 2024)
    financial_stability = st.slider("Financial Stability Score", 0, 100, 50)
    delivery_performance = st.slider("Delivery Performance Score", 0, 100, 50)
    quality_compliance = st.slider("Quality Compliance Score", 0, 100, 50)
    regulatory_adherence = st.slider("Regulatory Adherence Score", 0, 100, 50)

with col2:
    sustainability = st.slider("Sustainability Score", 0, 100, 50)
    past_risk_level = st.slider("Past Risk Level", 0, 10, 3)
    erp_transactions = st.slider("ERP Transactions", 0, 1000, 100)
    incidents = st.slider("Incidents Count", 0, 20, 2)
    mcdm = st.slider("MCDM Score", 0.0, 1.0, 0.5)

st.divider()

# Prediction button
if st.button("🔍 Predict Supplier Risk"):
    input_data = pd.DataFrame([[
        year,
        financial_stability,
        delivery_performance,
        quality_compliance,
        regulatory_adherence,
        sustainability,
        past_risk_level,
        erp_transactions,
        incidents,
        mcdm
    ]], columns=[
        'Year',
        'Financial_Stability_Score',
        'Delivery_Performance_Score',
        'Quality_Compliance_Score',
        'Regulatory_Adherence_Score',
        'Sustainability_Score',
        'Past_Risk_Level',
        'ERP_Transactions',
        'Incidents_Count',
        'MCDM_Score'
    ])

    prediction = model.predict(input_data)

    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.error("🚨 High Risk Supplier")
        st.write("Recommendation: Review supplier performance and consider mitigation strategies.")
    else:
        st.success("✅ Low / Medium Risk Supplier")
        st.write("Supplier risk is moderate. Continue monitoring operational indicators.")

st.divider()
st.markdown("### About the Model")
st.write("""
This model was trained using **Machine Learning algorithms** including:
- Logistic Regression
- Decision Tree
- Random Forest (selected as final model)

The system evaluates supplier risk using 10 operational and compliance indicators.
""")