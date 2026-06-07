
# Customer Churn Prediction System - Day 7

## Project Overview

The Customer Churn Prediction System is designed to predict whether a customer is likely to leave an e-commerce platform. Early identification of churn helps businesses improve customer retention and increase customer satisfaction.

## Dataset

* Dataset: E-commerce Customer Churn Dataset
* Total Records: 200,000
* Target Variable: Churn (0 = Not Churned, 1 = Churned)

## Algorithms Used

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Gradient Boosting

## Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

## Model Comparison Results

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 0.6551   |
| Decision Tree       | 0.5720   |
| Random Forest       | 0.6495   |
| Gradient Boosting   | 0.6581   |

## Final Model Selection

Logistic Regression was selected as the final model because it achieved competitive performance while providing better interpretability, faster training time, easier implementation, and simpler deployment compared to more complex models.

## Files Included

* customer_churn_day7.ipynb
* best_model.pkl
* confusion_matrix.png
* model_comparison.csv

## Future Improvements

* Hyperparameter tuning using GridSearchCV
* Cross-validation
* Feature engineering
* Deployment of the model using a web application

## Author

Nareddy Shanmukha Nihal Reddy
Innolift Ventures Internship - Track 2
