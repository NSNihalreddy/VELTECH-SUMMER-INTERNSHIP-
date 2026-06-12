# E-Commerce Customer Churn Prediction System - Day 12

## Project Overview

This project is a Flask-based E-Commerce Customer Churn Prediction System. Day 12 focused on integrating SQLite with the Flask application to store and retrieve customer data dynamically.

## Features Implemented

* Flask Routing
* HTML Templates
* CSS Styling
* SQLite Database Integration
* Customer Data Entry Form
* Dynamic Data Storage
* Dynamic Data Retrieval
* Customer Records Page
* Navigation Between Pages
* Responsive User Interface

## Project Structure

```text
EcommerceChurnApp/
│
├── app.py
├── database.py
├── churn.db
│
├── templates/
│   ├── index.html
│   ├── prediction.html
│   ├── dashboard.html
│   ├── about.html
│   └── customers.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
```

## Technologies Used

* Python
* Flask
* SQLite
* HTML5
* CSS3

## Database Functionality

The application uses SQLite to:

* Store customer information
* Retrieve customer records
* Display records dynamically using Flask templates

### Customer Fields

* Tenure
* Warehouse To Home
* Devices Registered
* Satisfaction Score
* Order Count
* Cashback Amount

## Testing Performed

* Added multiple customer records through the web form
* Verified successful insertion into SQLite database
* Verified dynamic retrieval of records
* Tested page navigation
* Tested multiple form submissions
* Confirmed successful database connectivity

## Outcome

Successfully developed a Flask application connected to SQLite for storing and displaying customer data. The system now supports dynamic backend operations and is ready for machine learning model integration in the next phase.

## Next Phase

* Integrate final_model.pkl
* Generate real-time churn predictions
* Display prediction results on the web interface
* Store prediction results in the database

## Author

Nareddy Shanmukha Nihal Reddy

Innolift Ventures Internship - Track 3
