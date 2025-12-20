# 🚗 Auto Insurance Claim Classification — End-to-End MLOps Project

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/your-username/your-repo-name/ci.yml?label=CI%2FCD)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-success)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange)

An end-to-end **Machine Learning + MLOps system** for predicting whether a customer will file an **auto insurance claim**.  
This project demonstrates a real-world ML lifecycle including **data ingestion, validation, training, CI/CD, deployment, monitoring, and UI integration**..

---

## 📌 **Project Highlights**

### ⭐ End-to-End MLOps Pipeline
- Automated data ingestion  
- Data validation with Great Expectations  
- Feature engineering pipeline  
- Model training with Scikit-Learn / XGBoost  
- Hyperparameter tuning  
- MLflow experiment tracking  
- MLflow model registry  

### ⭐ Deployment & Serving
- FastAPI model inference server  
- Docker containerization  
- Streamlit web UI  
- REST API for real-time predictions  

### ⭐ CI/CD & Testing
- GitHub Actions CI/CD pipeline  
- Linting, unit tests, automated builds  
- Docker image build pipeline  
- Test suite using PyTest  

### ⭐ Monitoring
- Data drift detection (Evidently AI)  
- Model drift & performance reporting  
- Logging & metrics collection  

---

## 📊 **Dataset**

You can use the publicly available Auto Insurance Claim dataset (Kaggle or similar).  
Typical features include:

- Age  
- Gender  
- Driving experience  
- Vehicle age  
- Vehicle damage  
- Annual premium  
- Policy sales channel  
- Previous claims  
- Target variable → **Claim (1) or No Claim (0)**  

---

## 🧠 **Problem Statement**

Insurance companies want to identify **high-risk policyholders** to:

- Optimize premiums  
- Reduce claim losses  
- Detect fraud  
- Improve underwriting decisions  

This ML model predicts **whether a customer will make an insurance claim**.

---

## 🏗️ **System Architecture**

