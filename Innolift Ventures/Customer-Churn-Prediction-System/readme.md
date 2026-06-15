# E-Commerce Customer Churn Prediction System

## Project Overview

The E-Commerce Customer Churn Prediction System is a Machine Learning-powered web application developed using Flask, SQLite, and Logistic Regression. The system predicts whether a customer is likely to churn based on customer behavior and engagement metrics.

The application provides real-time churn predictions, confidence scores, risk classification, customer analytics, and retention recommendations to help businesses identify and retain at-risk customers.

---

## Features

* Customer Churn Prediction using Machine Learning
* Real-Time Prediction Results
* Confidence Score Generation
* High, Medium, and Low Risk Classification
* Customer Risk Distribution Dashboard
* Customer Records Management
* Customer Record Deletion
* Risk-Based Customer Filtering
* Retention Recommendations
* Risk Factors Analysis
* Dynamic SQLite Database Integration
* Responsive and Professional User Interface

---

## Technology Stack

### Frontend

* HTML5
* CSS3

### Backend

* Flask (Python)

### Database

* SQLite

### Machine Learning

* Scikit-Learn
* Logistic Regression

### Libraries Used

* Pandas
* NumPy
* Joblib

---

## Project Structure

```text
EcommerceChurnApp/
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   ├── prediction.html
│   ├── dashboard.html
│   ├── customers.html
│   ├── risk_customers.html
│   └── about.html
│
├── app.py
├── database.py
├── churn.db
├── final_model.pkl
├── requirements.txt
└── README.md
```

---

## Application Workflow

Customer Input
↓
Prediction Form
↓
Flask Backend
↓
Machine Learning Model
↓
Prediction & Risk Analysis
↓
SQLite Database Storage
↓
Dashboard & Customer Records

---

## Risk Classification

| Risk Level  | Churn Probability |
| ----------- | ----------------- |
| High Risk   | ≥ 70%             |
| Medium Risk | 40% - 69%         |
| Low Risk    | < 40%             |

---

## Key Modules

### Home Page

Displays project overview and customer risk distribution.

### Prediction Page

Allows users to enter customer details and generate churn predictions.

### Dashboard

Displays customer statistics and business insights.

### Customer Records

Stores and manages customer prediction history.

### Risk Customers

Displays customers grouped by risk level.

### About Page

Provides project details and feature descriptions.

---

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create database

```bash
python database.py
```

4. Run application

```bash
python app.py
```

---

## Results

* Successfully integrated Machine Learning model with Flask.
* Implemented SQLite database operations.
* Generated real-time churn predictions.
* Implemented customer risk classification.
* Developed dynamic dashboard analytics.
* Built complete end-to-end workflow.


## Author

Nareddy Shanmukha Nihal Reddy

Innolift Ventures Internship Program

