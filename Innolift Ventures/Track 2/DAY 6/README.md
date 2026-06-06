# Day 6 - Algorithm Comparison

## Project
Customer Churn Prediction System

## Work Completed Today

- Loaded and analyzed the E-commerce Customer Churn dataset.
- Performed data preprocessing and converted categorical features into numerical format.
- Split the dataset into training and testing sets.
- Trained and evaluated four machine learning algorithms:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
- Compared model performance using Accuracy, Precision, Recall, and F1-Score.
- Generated a comparison table and exported the results to a CSV file.
- Analyzed the results and selected the most suitable model for the project.

## Model Comparison Results

| Model | Accuracy |
|---------|---------|
| Logistic Regression | 65.51% |
| Decision Tree | 57.20% |
| Random Forest | 64.95% |
| Gradient Boosting | 65.81% |

## Selected Model for Project

**Logistic Regression**

## Why Logistic Regression Was Chosen

Although Gradient Boosting achieved the highest accuracy (65.81%), the improvement over Logistic Regression (65.51%) was very small.

Logistic Regression was selected because:

- It provides performance comparable to Gradient Boosting.
- It is simple to understand and explain.
- It is easier to implement and maintain.
- It trains faster and requires fewer computational resources.
- It is suitable for a customer churn prediction project.

## Conclusion

Multiple machine learning algorithms were evaluated for customer churn prediction. While Gradient Boosting achieved the highest accuracy, Logistic Regression offered nearly the same performance with greater simplicity and interpretability. Therefore, Logistic Regression was selected as the final model for the project.
