import time
import random
import smtplib
from email.mime.text import MIMEText
import sqlite3
from flask import jsonify
import joblib
from flask import Flask, render_template, request, redirect, session, url_for,flash
import pandas as pd
from flask import session
from flask_bcrypt import Bcrypt
import database
import os
import base64

from dotenv import load_dotenv
from email.mime.text import MIMEText

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
# ===================== GMAIL API CONFIGURATION =====================

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


def get_gmail_service():

    token_path = "/etc/secrets/token.json"

    if not os.path.exists(token_path):
        token_path = "token.json"

    creds = Credentials.from_authorized_user_file(
        token_path,
        SCOPES
    )

    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    return service


def send_otp(email, otp):

    service = get_gmail_service()

    subject = "Email Verification OTP"

    body = f"""
Hello,

Your OTP for E-Commerce Customer Churn Prediction System is:

{otp}

This OTP is valid for 5 minutes.

If you didn't request this email, ignore it.

Thank you.
"""

    message = MIMEText(body)

    message["to"] = email
    message["from"] = EMAIL_ADDRESS
    message["subject"] = subject

    raw_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    service.users().messages().send(
        userId="me",
        body={"raw": raw_message}
    ).execute()

# ================================================================
        # Load ML Model
model = joblib.load("final_model.pkl")

print("Model Loaded Successfully")
print(type(model))
print(hasattr(model, "coef_"))
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "customer_churn_secret"
# Database Connection
def get_db_connection():
    conn = sqlite3.connect(
        "churn.db",
        timeout=30,
        check_same_thread=False
    )
    conn.row_factory = sqlite3.Row
    return conn
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        login_id = request.form["login_id"]
        password = request.form["password"]

        conn = get_db_connection()

        # Find user by email only
        user = conn.execute(
            """
            SELECT * FROM users
            WHERE email=?
            """,
            (login_id,)
        ).fetchone()

        conn.close()

        # Verify hashed password
        if user and bcrypt.check_password_hash(user["password"], password):

            session["user"] = user["email"]
            session["username"] = user["username"]
            session["user_id"] = user["id"]

            flash("Login Successful!", "success")
            return redirect("/home")

        else:
            flash("Invalid email or password.","error")
            return redirect("/")

    return render_template("login.html")
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()

        existing_user = conn.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        ).fetchone()

        conn.close()

        if existing_user:
            flash("Email already exists.", "error")
            return redirect("/register")

        otp = str(random.randint(100000, 999999))

        session["register_data"] = {
            "username": username,
            "email": email,
            "password": password
        }

        session["register_otp"] = otp
        session["otp_type"] = "register"
        session["otp_time"] = time.time()
        session["resend_count"] = 0
        send_otp(email, otp)

        flash("OTP has been sent to your email.", "success")

        return redirect(url_for("verify_otp"))

    return render_template("register.html")
@app.route("/verify_otp", methods=["GET", "POST"])
def verify_otp():

    if "otp_type" not in session:
        flash("Session expired. Please try again.", "error")
        return redirect(url_for("register"))

    if request.method == "POST":

        # Check OTP expiry
        if time.time() - session.get("otp_time", 0) > 300:
            flash("OTP has expired. Please resend a new OTP.", "error")
            return redirect(url_for("verify_otp"))

        entered_otp = request.form["otp"]

        # ---------------- REGISTER ----------------
        if session["otp_type"] == "register":

            if entered_otp != session.get("register_otp"):
                flash("Invalid OTP.", "error")
                return redirect(url_for("verify_otp"))

            data = session["register_data"]

            hashed_password = bcrypt.generate_password_hash(
                data["password"]
            ).decode("utf-8")

            conn = get_db_connection()

            conn.execute(
                """
                INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)
                """,
                (
                    data["username"],
                    data["email"],
                    hashed_password
                )
            )

            conn.commit()
            conn.close()

            session.pop("register_data", None)
            session.pop("register_otp", None)
            session.pop("otp_time", None)
            session.pop("resend_count", None)
            session.pop("otp_type", None)

            flash("Registration Successful.", "success")

            return redirect(url_for("login"))

        # ---------------- FORGOT PASSWORD ----------------
        elif session["otp_type"] == "forgot":

            if entered_otp != session.get("forgot_otp"):
                flash("Invalid OTP.", "error")
                return redirect(url_for("verify_otp"))

            return redirect(url_for("reset_password"))

    # Show masked email
    if session["otp_type"] == "register":
        email = session["register_data"]["email"]
    else:
        email = session["forgot_email"]

    name, domain = email.split("@")
    masked_email = name[:2] + "*" * (len(name) - 2) + "@" + domain

    return render_template(
        "verify_otp.html",
        masked_email=masked_email
    )
@app.route("/resend_otp")
def resend_otp():

    data = session.get("register_data")

    if not data:
        return jsonify({
            "status": "error",
            "message": "Registration session expired."
        })

    resend_count = session.get("resend_count", 0)

    if resend_count >= 5:
        return jsonify({
            "status": "error",
            "message": "Maximum resend attempts reached."
        })

    otp = str(random.randint(100000,999999))

    session["register_otp"] = otp
    session["otp_time"] = time.time()
    session["resend_count"] = resend_count + 1

    if session["otp_type"] == "register":
        email = session["register_data"]["email"]
    else:
        email = session["forgot_email"]

    send_otp(email, otp)

    return jsonify({
        "status":"success",
        "message":"A new OTP has been sent."
    })
@app.route("/reset_password", methods=["GET","POST"])
def reset_password():

    if "forgot_email" not in session:
        flash("Session expired.","error")
        return redirect(url_for("forgot_password"))

    if request.method=="POST":

        password=request.form["password"]
        confirm=request.form["confirm_password"]

        if password!=confirm:

            flash("Passwords do not match.","error")
            return redirect(url_for("reset_password"))

        hashed=bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

        conn=get_db_connection()

        conn.execute(
            """
            UPDATE users
            SET password=?
            WHERE email=?
            """,
            (
                hashed,
                session["forgot_email"]
            )
        )

        conn.commit()
        conn.close()

        session.pop("forgot_email",None)
        session.pop("forgot_otp",None)
        session.pop("otp_time",None)
        session.pop("otp_type",None)
        session.pop("resend_count",None)

        flash(
            "Password updated successfully.",
            "success"
        )

        return redirect(url_for("login"))

    return render_template("reset_password.html")
@app.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully.", "info")

    return redirect(url_for("login"))

@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form["email"]

        conn = get_db_connection()

        user = conn.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        ).fetchone()

        conn.close()

        if not user:

            flash("Email not found.", "error")
            return redirect(url_for("forgot_password"))

        otp = str(random.randint(100000, 999999))

        session["forgot_email"] = email
        session["forgot_otp"] = otp
        session["otp_type"] = "forgot"
        session["otp_time"] = time.time()
        session["resend_count"] = 0

        send_otp(email, otp)

        flash("OTP sent to your email.", "success")

        return redirect(url_for("verify_otp"))

    return render_template("forgot_password.html")
    
# =========================
# HOME PAGE
# =========================
@app.route('/home')
def home():

    if "user_id" not in session:
        return redirect("/")

    conn = get_db_connection()

    total_customers = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE user_id=?",
        (session["user_id"],)
    ).fetchone()[0]

    churned_customers = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE user_id=? AND prediction='Churn'",
        (session["user_id"],)
    ).fetchone()[0]

    retained_customers = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE user_id=? AND prediction='No Churn'",
        (session["user_id"],)
    ).fetchone()[0]

    high_risk = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE user_id=? AND risk_level='High Risk'",
        (session["user_id"],)
    ).fetchone()[0]

    medium_risk = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE user_id=? AND risk_level='Medium Risk'",
        (session["user_id"],)
    ).fetchone()[0]

    low_risk = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE user_id=? AND risk_level='Low Risk'",
        (session["user_id"],)
    ).fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        total_customers=total_customers,
        churned_customers=churned_customers,
        retained_customers=retained_customers,
        high_risk=high_risk,
        medium_risk=medium_risk,
        low_risk=low_risk
    )

# =========================
# PREDICTION PAGE
# =========================
@app.route('/prediction')
def prediction():
    return render_template('prediction.html')


# =========================
# PREDICT CUSTOMER CHURN
# =========================
@app.route('/predict', methods=['POST'])
def predict():
    if "user" not in session:
        return redirect("/")

    customer_id = int(request.form['customer_id'])
    age = int(request.form['age'])
    tenure_months = int(request.form['tenure_months'])
    avg_order_value = float(request.form['avg_order_value'])
    total_orders = int(request.form['total_orders'])
    last_purchase_days_ago = int(request.form['last_purchase_days_ago'])
    support_tickets = int(request.form['support_tickets'])

    gender = request.form['gender']
    city = request.form['city']
    subscription_type = request.form['subscription_type']

    input_data = pd.DataFrame([{

        'customer_id': customer_id,
        'age': age,
        'tenure_months': tenure_months,
        'avg_order_value': avg_order_value,
        'total_orders': total_orders,
        'last_purchase_days_ago': last_purchase_days_ago,
        'support_tickets': support_tickets,

        'gender_Male': 1 if gender == "Male" else 0,

        'city_Chennai': 1 if city == "Chennai" else 0,
        'city_Delhi': 1 if city == "Delhi" else 0,
        'city_Hyderabad': 1 if city == "Hyderabad" else 0,
        'city_Kolkata': 1 if city == "Kolkata" else 0,
        'city_Mumbai': 1 if city == "Mumbai" else 0,
        'city_Pune': 1 if city == "Pune" else 0,

        'subscription_type_Gold': 1 if subscription_type == "Gold" else 0,
        'subscription_type_Platinum': 1 if subscription_type == "Platinum" else 0,
        'subscription_type_Silver': 1 if subscription_type == "Silver" else 0

    }])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    confidence = round(max(probability) * 100, 2)

    churn_probability = round(probability[1] * 100, 2)

    result = "Churn" if prediction == 1 else "No Churn"
    # Risk Level Classification

    if churn_probability >= 70:
        risk_level = "High Risk"

    elif churn_probability >= 40:
        risk_level = "Medium Risk"

    else:
        risk_level = "Low Risk"
    print("Risk Level:", risk_level)
    print("Churn Probability:", churn_probability)
    # Risk Factors
    risk_factors = []

    if tenure_months < 6:
        risk_factors.append("Low customer tenure")

    if total_orders < 5:
        risk_factors.append("Low purchase frequency")

    if support_tickets > 5:
        risk_factors.append("High support ticket count")

    if last_purchase_days_ago > 60:
        risk_factors.append("Customer inactivity")

    if avg_order_value < 500:
        risk_factors.append("Low spending behavior")

    if len(risk_factors) == 0:
        risk_factors.append("Customer shows stable engagement")

    risk_factors = risk_factors[:3]

    # Recommended Actions
    recommended_actions = []

    if support_tickets > 5:
        recommended_actions.append(
            "Improve customer support experience"
        )

    if total_orders < 5:
        recommended_actions.append(
            "Provide personalized discounts and offers"
        )

    if last_purchase_days_ago > 60:
        recommended_actions.append(
            "Launch customer re-engagement campaigns"
        )

    if tenure_months < 6:
        recommended_actions.append(
            "Offer loyalty rewards and onboarding benefits"
        )

    if len(recommended_actions) == 0:
        recommended_actions.append(
            "Maintain current customer engagement strategy"
        )

    recommended_actions = recommended_actions[:3]

    # Save into database
    conn = get_db_connection()
    user_id = session["user_id"]
    conn.execute("""
INSERT INTO customers (
    user_id,
    customer_id,
    age,
    tenure_months,
    avg_order_value,
    total_orders,
    last_purchase_days_ago,
    support_tickets,
    gender,
    city,
    subscription_type,
    prediction,
    confidence,
    risk_level
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""",
(
    session["user_id"],
    customer_id,
    age,
    tenure_months,
    avg_order_value,
    total_orders,
    last_purchase_days_ago,
    support_tickets,
    gender,
    city,
    subscription_type,
    result,
    confidence,
    risk_level
))

    conn.commit()
    conn.close()

    return render_template(
        'prediction.html',
        prediction=result,
        confidence=confidence,
        risk_factors=risk_factors,
        recommended_actions=recommended_actions
    )

# =========================
# DASHBOARD PAGE
# =========================
@app.route('/dashboard')
def dashboard():

    if "user_id" not in session:
        return redirect("/")

    conn = get_db_connection()

    total_customers = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE user_id=?",
        (session["user_id"],)
    ).fetchone()[0]

    churned_customers = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE user_id=? AND prediction='Churn'",
        (session["user_id"],)
    ).fetchone()[0]

    retained_customers = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE user_id=? AND prediction='No Churn'",
        (session["user_id"],)
    ).fetchone()[0]

    if total_customers > 0:
        churn_rate = round(
            (churned_customers / total_customers) * 100,
            2
        )
    else:
        churn_rate = 0

    conn.close()

    return render_template(
        'dashboard.html',
        total_customers=total_customers,
        churned_customers=churned_customers,
        retained_customers=retained_customers,
        churn_rate=churn_rate
    )

# =========================
# ABOUT PAGE
# =========================
@app.route('/about')
def about():
    return render_template('about.html')

    if "user" not in session:
        return redirect("/")
# =========================
# CUSTOMER RECORDS PAGE
# =========================
@app.route('/customers')
def customers():

    if "user_id" not in session:
        return redirect("/")

    conn = get_db_connection()

    customers = conn.execute(
        """
        SELECT * FROM customers
        WHERE user_id=?
        """,
        (session["user_id"],)
    ).fetchall()

    conn.close()

    return render_template(
        "customers.html",
        customers=customers
    )
@app.route('/risk/<level>')
def risk_customers(level):

    if "user_id" not in session:
        return redirect("/")

    conn = get_db_connection()

    if level == "high":

        customers = conn.execute("""
            SELECT *
            FROM customers
            WHERE user_id=? AND risk_level='High Risk'
            ORDER BY id ASC
        """, (session["user_id"],)).fetchall()

    elif level == "medium":

        customers = conn.execute("""
            SELECT *
            FROM customers
            WHERE user_id=? AND risk_level='Medium Risk'
            ORDER BY id ASC
        """, (session["user_id"],)).fetchall()

    else:

        customers = conn.execute("""
            SELECT *
            FROM customers
            WHERE user_id=? AND risk_level='Low Risk'
            ORDER BY id ASC
        """, (session["user_id"],)).fetchall()

    conn.close()

    return render_template(
        "risk_customers.html",
        customers=customers,
        level=level
    )
    
    

# =========================
# DELETE CUSTOMER
# =========================
@app.route('/delete_customer/<int:id>', methods=['POST'])
def delete_customer(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM customers WHERE id=? AND user_id=?",
        (id, session["user_id"])
    )

    conn.commit()
    conn.close()

    return redirect(url_for('customers'))
# =========================
# RUN APP
# =========================
if __name__ == '__main__':
    app.run(debug=True)