import sqlite3
from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd

# Load ML Model
model = joblib.load("final_model.pkl")

print("Model Loaded Successfully")
print(type(model))
print(hasattr(model, "coef_"))

app = Flask(__name__)


# Database Connection
def get_db_connection():
    conn = sqlite3.connect("churn.db")
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# HOME PAGE
# =========================
@app.route('/')
def home():

    conn = get_db_connection()

    total_customers = conn.execute(
        "SELECT COUNT(*) FROM customers"
    ).fetchone()[0]

    churned_customers = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE prediction='Churn'"
    ).fetchone()[0]

    retained_customers = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE prediction='No Churn'"
    ).fetchone()[0]
    
    high_risk = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE risk_level='High Risk'"
).fetchone()[0]

    medium_risk = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE risk_level='Medium Risk'"
).fetchone()[0]

    low_risk = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE risk_level='Low Risk'"
).fetchone()[0]
    conn.close()

    return render_template(
        'index.html',
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

    conn.execute("""
    INSERT INTO customers
    (
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
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""",
(
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

    conn = get_db_connection()

    total_customers = conn.execute(
        "SELECT COUNT(*) FROM customers"
    ).fetchone()[0]

    churned_customers = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE prediction='Churn'"
    ).fetchone()[0]

    retained_customers = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE prediction='No Churn'"
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


# =========================
# CUSTOMER RECORDS PAGE
# =========================
@app.route('/customers')
def customers():

    conn = get_db_connection()

    customers = conn.execute(
        "SELECT * FROM customers ORDER BY id ASC"
    ).fetchall()

    conn.close()

    return render_template(
        'customers.html',
        customers=customers
    )
@app.route('/risk/<level>')
def risk_customers(level):

    conn = get_db_connection()

    if level == "high":

        customers = conn.execute("""
            SELECT *
            FROM customers
            WHERE risk_level='High Risk'
            ORDER BY id ASC
        """).fetchall()

    elif level == "medium":

        customers = conn.execute("""
            SELECT *
            FROM customers
            WHERE risk_level='Medium Risk'
            ORDER BY id ASC
        """).fetchall()

    else:

        customers = conn.execute("""
            SELECT *
            FROM customers
            WHERE risk_level='Low Risk'
            ORDER BY id ASC
        """).fetchall()

    conn.close()

    return render_template(
        'risk_customers.html',
        customers=customers,
        level=level
    )

# =========================
# DELETE CUSTOMER
# =========================
@app.route('/delete_customer/<int:id>')
def delete_customer(id):

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM customers WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for('customers'))


# =========================
# RUN APP
# =========================
if __name__ == '__main__':
    app.run(debug=True)