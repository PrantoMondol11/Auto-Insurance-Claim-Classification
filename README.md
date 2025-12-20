# Vehicle Data MLOps Platform

## Overview

This project implements a **full-stack MLOps platform** that automates the complete machine learning lifecycle — from **data ingestion** to **model deployment** — using **cloud-native, secure, and scalable engineering practices**.

The system is designed to closely mirror **real-world production ML workflows**, emphasizing **automation, reproducibility, security, CI/CD, and maintainability**.
It demonstrates hands-on experience with **Dockerized deployments**, **AWS IAM-secured infrastructure**, **MongoDB Atlas**, and **GitHub Actions**.

---

## Key Capabilities

* Automated end-to-end ML pipeline
* Cloud-based data ingestion from MongoDB Atlas
* Schema-driven data validation
* Feature engineering and transformation pipelines
* Model training and threshold-based evaluation
* Model versioning using AWS S3
* Secure containerized deployment using Docker
* CI/CD pipeline with AWS ECR and EC2
* API-based prediction and retraining

---

## System Architecture

```
MongoDB Atlas
     │
     ▼
Data Ingestion
     │
     ▼
Data Validation (Schema & Consistency)
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
AWS EC2 (Flask Prediction Service)
```

---

## Technology Stack

### Programming & Machine Learning

* Python 3.10
* Pandas, NumPy
* Scikit-learn

### Database

* **MongoDB Atlas**

  * Cloud-hosted NoSQL database
  * Secure user authentication
  * Network access control
  * Python-based ingestion

### Cloud & DevOps (AWS)

* **IAM** – Identity and Access Management
* **ECR** – Private Docker image registry
* **S3** – Model registry and version control
* **EC2** – Production deployment server

### CI/CD & Containerization

* **Docker**
* **GitHub Actions**
* Self-hosted GitHub Runner on EC2

---

## Containerization with Docker

The application is fully containerized using **Docker** to ensure environment consistency across development, testing, and production.

### Docker Implementation

* A production-ready `Dockerfile` is used to:

  * Install system and Python dependencies
  * Copy application source code
  * Expose application port
  * Launch the Flask application
* A `.dockerignore` file minimizes image size and improves build efficiency
* Docker images are built automatically as part of the CI/CD pipeline

### Docker + AWS ECR Workflow

* Docker images are authenticated and pushed to **AWS ECR** using **IAM credentials**
* EC2 instances securely pull images from ECR for deployment
* Ensures reproducibility, scalability, and simplified rollback

---

## Security & IAM Practices

Security is implemented using **AWS IAM best practices**.

### IAM Usage

* Dedicated IAM users created for:

  * CI/CD pipeline execution
  * ECR image push/pull
  * S3 model access
* Credentials managed using:

  * GitHub Secrets
  * Environment variables
* No secrets or keys are hard-coded in the repository

### ECR Security

* Private ECR repository
* IAM-authenticated Docker login
* Controlled access to container images

---

## CI/CD Pipeline

A fully automated **CI/CD pipeline** is implemented using GitHub Actions.

### Pipeline Flow

1. Code push to GitHub
2. Build Docker image
3. Authenticate with AWS ECR using IAM
4. Push Docker image to ECR
5. Deploy updated container on EC2

The pipeline runs on a **self-hosted EC2 runner**, providing production-level control and reliability.

---

## Project Structure

```
src/
├── components/           # ML pipeline components
├── configuration/        # MongoDB & AWS configurations
├── data_access/          # Database interaction layer
├── entity/               # Config & artifact definitions
├── aws_storage/          # S3 and ECR utilities
├── utils/                # Common helper functions
├── logger/               # Centralized logging
└── exception/            # Custom exception handling
```

Designed using:

* Separation of concerns
* Configuration-driven architecture
* Artifact-based pipeline tracking

---

## Core MLOps Features

* Modular, reusable pipeline components
* YAML-based schema validation
* Robust logging and exception handling
* Automated feature engineering
* Model evaluation with configurable thresholds
* Cloud-based model registry with versioning
* API-triggered retraining
* Secure and reproducible deployments

---

## Running the Project Locally

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

Access the application at:

```
http://localhost:5080
```

---

## API Endpoints

| Endpoint    | Description              |
| ----------- | ------------------------ |
| `/`         | Home                     |
| `/predict`  | Generate predictions     |
| `/training` | Trigger full ML pipeline |

---

## Why This Project Is Production-Ready

* Reflects real enterprise ML workflows
* Demonstrates cloud security and IAM knowledge
* Implements CI/CD for ML systems
* Uses Docker for environment consistency
* Emphasizes maintainability and scalability
* Aligns with industry MLOps standards

---

## Author

**Pranto Mondol**
Machine Learning Engineer | MLOps Engineer

Email: [mondolpranto83@gmail.com]
LinkedIn: [https://www.linkedin.com/in/pranto-mondol-devops/]
