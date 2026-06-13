# E-Commerce Customer Churn Prediction System

## Project Overview

The E-Commerce Customer Churn Prediction System is a Machine Learning-based web application developed using Flask, SQLite, and Logistic Regression. The system predicts whether a customer is likely to leave the company (Churn) or continue using its services (No Churn).

The application provides customer churn prediction, customer record management, database storage, and a real-time dashboard for monitoring churn statistics.

---

## Features

* Machine Learning-based Churn Prediction
* Logistic Regression Model Integration
* Real-Time Prediction Results
* Customer Record Management
* Delete Customer Records
* Dynamic Dashboard Analytics
* SQLite Database Integration
* Responsive User Interface
* Flask Web Application

---

## Technologies Used

* Python
* Flask
* SQLite
* Pandas
* Scikit-Learn
* Joblib
* HTML5
* CSS3

---

## Machine Learning Model

**Algorithm:** Logistic Regression

### Input Features

* Customer ID
* Age
* Tenure Months
* Average Order Value
* Total Orders
* Last Purchase Days Ago
* Support Tickets
* Gender
* City
* Subscription Type

### Prediction Output

* Churn
* No Churn

---

## Project Structure

```text
EcommerceChurnApp/
│
├── static/
│   ├── css/
│   │   └── style.css
│
├── templates/
│   ├── index.html
│   ├── prediction.html
│   ├── dashboard.html
│   ├── customers.html
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

## Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Install Required Libraries

```bash
pip install flask pandas scikit-learn joblib
```

### Create Database

```bash
python database.py
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## Dashboard Metrics

The dashboard dynamically updates using customer prediction records and displays:

* Total Customers
* Churned Customers
* Retained Customers
* Churn Rate

---

## Project Workflow

1. Enter customer details.
2. Submit the prediction form.
3. Machine Learning model predicts churn status.
4. Prediction result and confidence score are generated.
5. Customer record is stored in SQLite database.
6. Dashboard updates automatically.
7. Records can be viewed or deleted from the Customers page.

---

## Internship Project

This project was developed as part of the Innolift Ventures Internship Program to demonstrate the integration of Machine Learning models with a Flask web application and SQLite database.

---

## Author

**Nareddy Shanmukha Nihal Reddy**
