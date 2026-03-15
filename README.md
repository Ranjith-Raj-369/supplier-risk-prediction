# AI Supplier Risk Prediction Dashboard

## Application Preview

![Dashboard](images/dashboard.png)

---

## Overview

The **AI Supplier Risk Prediction Dashboard** is a machine learning application that predicts the **risk level of suppliers** based on operational, financial, and compliance indicators.

This system helps supply chain managers identify **high-risk suppliers early** and take preventive actions to reduce supply chain disruptions.

The application is deployed as an **interactive web dashboard using Streamlit**, allowing users to input supplier metrics and obtain real-time risk predictions.

---

## Problem Statement

Supplier risk management is critical for organizations operating in global supply chains. Poor supplier performance can lead to:

* Operational disruptions
* Financial losses
* Compliance violations
* Delivery delays

This project builds an **AI-driven supplier risk prediction system** to support proactive decision-making.

---

## Machine Learning Workflow

The project follows a complete machine learning pipeline:

1. Data Exploration
2. Data Preprocessing
3. Feature Scaling
4. Model Training
5. Model Evaluation
6. Feature Importance Analysis
7. Model Deployment

---

## Machine Learning Models Used

Three models were trained and evaluated:

* Logistic Regression
* Decision Tree
* Random Forest

The **Random Forest model** was selected as the final model due to its strong performance and ability to capture complex relationships between supplier metrics.

---

## Feature Importance Insights

The Random Forest model identified the following features as the most influential predictors of supplier risk:

* MCDM Score
* Financial Stability Score
* Delivery Performance Score

These metrics play a key role in determining supplier reliability.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib
* Matplotlib

---

## Project Structure

supplier-risk-prediction-app

app.py
supplier_risk_model.pkl
requirements.txt
README.md
images/dashboard.png

---

## How the Application Works

1. The user enters supplier performance indicators using sliders.
2. The machine learning model processes the inputs.
3. The system predicts whether the supplier is **High Risk** or **Low/Medium Risk**.
4. A recommendation message is displayed to assist decision-making.

---

## Example Use Case

Supply chain teams can use this tool to:

* Evaluate new suppliers
* Monitor supplier performance
* Identify potential risks early
* Support procurement decisions

---

## Deployment

The application is deployed using **Streamlit Community Cloud**, allowing users to access the model through a web interface.

Live Application:
(Add your Streamlit deployment link here)

---

## Skills Demonstrated

* Machine Learning Model Development
* Data Preprocessing & Feature Scaling
* Model Evaluation (Accuracy, Confusion Matrix)
* Feature Importance Analysis
* Model Serialization
* Interactive Dashboard Development
* AI Model Deployment

---

## Author

Ranjith Raj

Data and AI enthusiast
