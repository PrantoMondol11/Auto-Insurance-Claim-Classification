<div align="center">

# 🚗 Vehicle Data MLOps Platform

### End-to-End Production-Grade Machine Learning System

**Cloud-Native • Secure • Automated • Scalable**

<br/>

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![AWS](https://img.shields.io/badge/AWS-IAM%20%7C%20ECR%20%7C%20S3-orange)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-success)
![MongoDB](https://img.shields.io/badge/Database-MongoDB%20Atlas-brightgreen)

</div>

---

## 📌 Overview

This repository contains a **production-grade MLOps platform** implementing the **complete machine learning lifecycle** — from data ingestion to model deployment — using **modern cloud and DevOps best practices**.

The project emphasizes:

* **Automation**
* **Security**
* **Reproducibility**
* **Scalability**
* **Maintainability**

It is designed to reflect **real-world ML systems used in production environments**.

---

## ✨ Key Capabilities

✔ Automated end-to-end ML pipelines
✔ Cloud-based data ingestion from MongoDB Atlas
✔ Schema-driven data validation
✔ Feature engineering & transformation
✔ Model training & evaluation
✔ Model versioning using AWS S3
✔ Secure Dockerized deployment
✔ CI/CD with GitHub Actions & AWS ECR
✔ REST-based prediction & retraining APIs

---

## 🏗️ System Architecture

```
MongoDB Atlas
     │
     ▼
Data Ingestion
     │
     ▼
Data Validation
     │
     ▼
Data Transformation
     │
     ▼
Model Trainer
     │
     ▼
Model Evaluation
     │
     ▼
AWS S3 (Model Registry)
     │
     ▼
Model Pusher
     │
     ▼
Docker Image
     │
     ▼
AWS ECR (IAM Secured)
     │
     ▼
AWS EC2 (Flask App)
```

---

## 🛠️ Technology Stack

### 🔹 Programming & ML

* Python 3.10
* Pandas, NumPy
* Scikit-learn

### 🔹 Database

* **MongoDB Atlas**

  * Cloud-hosted NoSQL database
  * Secure authentication & network access
  * Python-based ingestion

### 🔹 Cloud & DevOps

* **AWS IAM** – Secure access control
* **AWS ECR** – Private Docker image registry
* **AWS S3** – Model registry & versioning
* **AWS EC2** – Production deployment

### 🔹 CI/CD & Containerization

* **Docker**
* **GitHub Actions**
* Self-hosted GitHub Runner on EC2

---

## 🐳 Containerization with Docker

The application is fully containerized using **Docker** to ensure consistent behavior across all environments.

**Docker highlights:**

* Production-ready `Dockerfile`
* Optimized `.dockerignore`
* Automated image builds via CI/CD
* Secure image storage in AWS ECR
* EC2-based container deployment

---

## 🔐 Security & IAM Practices

Security is implemented using **AWS IAM best practices**.

### IAM Implementation

* Dedicated IAM users for:

  * CI/CD pipelines
  * ECR image operations
  * S3 model access
* Secrets managed via:

  * GitHub Secrets
  * Environment variables
* **No hard-coded credentials**

### ECR Security

* Private repositories
* IAM-authenticated Docker login
* Controlled push/pull access

---

## 🔁 CI/CD Pipeline

A fully automated CI/CD pipeline is implemented using **GitHub Actions**.

### Workflow

1. Code pushed to GitHub
2. Docker image build
3. IAM-based authentication to AWS ECR
4. Image pushed to ECR
5. Deployment on EC2

Runs on a **self-hosted EC2 runner**, ensuring production-grade deployment behavior.

---

## 📂 Project Structure

```
src/
├── components/        # ML pipeline stages
├── configuration/     # MongoDB & AWS configs
├── data_access/       # Database interaction
├── entity/            # Config & artifacts
├── aws_storage/       # S3 & ECR utilities
├── utils/             # Shared utilities
├── logger/            # Logging
└── exception/         # Exception handling
```

Designed using:

* Separation of concerns
* Configuration-driven design
* Artifact-based pipelines

---

## ⚙️ Core MLOps Features

* Modular ML pipelines
* YAML-based schema validation
* Robust logging & exception handling
* Automated feature engineering
* Threshold-based model evaluation
* Cloud-based model registry
* API-triggered retraining
* Secure, reproducible deployments

---

## 🚀 Running the Project

### Environment Setup

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
```

### Run Training Pipeline

```bash
python demo.py
```

### Start Prediction Service

```bash
python app.py
```

Access:

```
http://localhost:5080
```

---

## 🌐 API Endpoints

| Endpoint    | Description                    |
| ----------- | ------------------------------ |
| `/`         | Home                           |
| `/predict`  | Generate predictions           |
| `/training` | Trigger full training pipeline |

---

## 🎯 Why This Project Stands Out

* Mirrors real-world enterprise MLOps systems
* Demonstrates secure cloud deployment (IAM + ECR)
* Uses CI/CD for ML workflows
* Dockerized for reproducibility
* Clean, maintainable architecture
* Strong emphasis on production readiness

---

## 👨‍💻 Author

**Pranto Mondol**
Machine Learning Engineer | MLOps Engineer

📧 [mondolpranto83@gmail.com]
🔗 [https://www.linkedin.com/in/pranto-mondol-devops/]

---

