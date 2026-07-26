# Ecommerce Customer Churn Predictor

A Flask-based web application that predicts customer churn using Machine Learning while providing a secure authentication system with OTP-based email verification.

---

## 📌 Overview

The Ecommerce Customer Churn Predictor helps businesses identify customers who are likely to stop using their services. It uses a trained Machine Learning model to analyze customer information and predict churn probability. The application also includes a complete user authentication system with Gmail API-based OTP verification for secure account management.

---

## ✨ Features

### 🔐 Authentication
- User Registration
- Email OTP Verification
- Secure Login
- Forgot Password
- OTP-Based Password Reset
- Password Strength Indicator
- Password Match Validation
- Show/Hide Password
- Secure Password Hashing using bcrypt

### 📊 Churn Prediction
- Customer Churn Prediction
- Machine Learning Model Integration
- Prediction Dashboard
- Customer Management
- User-specific Prediction History

### 🎨 User Interface
- Responsive Design
- Glassmorphism UI
- Modern Dashboard
- Interactive Forms
- Clean Navigation

---

## 🛠 Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- SQLite
- Scikit-learn
- Pandas
- NumPy
- Gmail API
- Git & GitHub

---

## 🤖 Machine Learning

The project uses a trained Machine Learning model to predict customer churn based on customer details. The dataset was preprocessed, analyzed, and used to train the prediction model before deployment.

---

## 📂 Project Structure

```text
EcommerceChurnApp/
│
├── app.py
├── database.py
├── gmail_auth.py
├── requirements.txt
├── best_model.pkl
├── churn.db
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── verify_otp.html
│   ├── forgot_password.html
│   ├── reset_password.html
│   ├── dashboard.html
│   └── ...
│
└── README.md
```

---

## 🚀 Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/ecommerce-churn-predictor.git
```

2. Navigate to the project folder

```bash
cd ecommerce-churn-predictor
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python app.py
```

5. Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📧 Gmail API Configuration

This project uses the Gmail API to send OTP emails for registration and password recovery.

Before running the project:

- Configure Google Cloud Console.
- Enable the Gmail API.
- Download the OAuth credentials (`credentials.json`).
- Complete the authorization process to generate `token.json`.

---

## 🔮 Future Enhancements

- Email Notifications
- PDF Report Generation
- Advanced Analytics Dashboard
- Cloud Database Integration
- Admin Panel
- Model Performance Comparison

---

## 👨‍💻 Author

**Nareddy Shanmukha Nihal Reddy**

B.Tech – Computer Science & Engineering (AI & Data Science)

Vel Tech University

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
