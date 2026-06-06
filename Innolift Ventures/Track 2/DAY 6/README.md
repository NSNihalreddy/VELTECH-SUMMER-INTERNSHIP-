# Day 6 - Algorithm Comparison

## Objective
Compare multiple machine learning algorithms for the Customer Churn Prediction project and identify the best-performing model.

## Dataset
E-commerce Customer Churn Dataset

## Steps Performed
1. Loaded the dataset into Google Colab.
2. Identified the target column (churn).
3. Separated features and target variables.
4. Converted categorical data into numerical format using one-hot encoding.
5. Split the dataset into training and testing sets.
6. Trained the following models:
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - Gradient Boosting
7. Evaluated models using:
   - Accuracy
   - Precision
   - Recall
   - F1-Score
8. Created a comparison table and exported it to CSV.
9. Selected the best-performing model.

## Results

| Model | Accuracy |
|---------|---------|
| Logistic Regression | 65.51% |
| Decision Tree | 57.20% |
| Random Forest | 64.95% |
| Gradient Boosting | 65.81% |

## Best Model
Gradient Boosting achieved the highest accuracy (65.81%) and was selected as the best-performing model.

## Files Included
- day6_algorithm_comparison.ipynb
- model_comparison.csv
- Comparison table screenshot
- Best model screenshot
