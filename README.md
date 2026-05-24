# Customer Churn Prediction using Machine Learning

## Project Title

Customer Churn Prediction using Machine Learning

## Author(s)

Suhani Bode

## Affiliation

Rashtrasant Tukadoji Maharaj Nagpur University

## Date

May 2026

---

# Abstract

This project presents a supervised machine learning classification model for predicting customer churn. Customer churn prediction is an important problem for businesses because retaining customers is more cost-effective than acquiring new ones. The project uses the Telco Customer Churn dataset containing customer details such as tenure, contract type, monthly charges, payment methods, and internet services.

The dataset was preprocessed by handling missing values, converting categorical variables into numerical form, and applying feature scaling techniques. Two machine learning algorithms, Logistic Regression and Random Forest Classifier, were implemented and compared.

The dataset was divided into training and testing sets using train-test split, and cross-validation was performed for reliable evaluation. Performance metrics including Accuracy, Precision, Recall, F1 Score, and ROC-AUC were used to measure model effectiveness.

The results showed that Logistic Regression achieved slightly better performance compared to Random Forest. This project helped in understanding the complete machine learning workflow including preprocessing, model training, evaluation, and comparison of classification algorithms.

---

# Introduction

Customer churn refers to customers discontinuing the use of a company's services. Predicting customer churn is important for organizations because customer retention directly affects business revenue and growth.

With the increase in digital services and competition among companies, machine learning techniques have become highly useful for analyzing customer behavior and predicting churn. Accurate churn prediction helps companies take preventive actions and improve customer satisfaction.

The main objective of this project is to build and evaluate supervised machine learning classification models capable of predicting whether a customer will churn based on available customer information.

---

# Literature Review

Many organizations use machine learning techniques for churn prediction. Traditional statistical approaches such as Logistic Regression are commonly used because of their simplicity and interpretability. Ensemble methods like Random Forest have also gained popularity due to their ability to handle complex relationships in data.

Previous studies have shown that feature engineering, preprocessing, and model selection play important roles in improving prediction accuracy. Researchers have also explored advanced algorithms such as XGBoost, Support Vector Machines, and Neural Networks for churn analysis.

This project focuses on implementing and comparing Logistic Regression and Random Forest models for customer churn prediction using structured customer data.

---

# Methodology

The project follows a supervised machine learning workflow for customer churn prediction. The dataset was first cleaned and preprocessed by removing unnecessary columns, handling missing values, scaling numerical features, and encoding categorical variables. The processed data was divided into training and testing sets using train-test split. Logistic Regression and Random Forest classification algorithms were trained on the training dataset. Predictions were made on the testing dataset, and the models were evaluated using Accuracy, Precision, Recall, F1 Score, and ROC-AUC metrics. Cross-validation was also performed to improve the reliability and consistency of the evaluation process.

---

# Implementation

## Programming Languages

* Python

## Frameworks/Libraries

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

## Tools Used

* Google Colab
* GitHub

---

# Results and Discussion

Two machine learning algorithms were implemented and compared:

1. Logistic Regression
2. Random Forest Classifier

The models were evaluated using multiple performance metrics.

| Model               | Accuracy | Precision | Recall | F1 Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 0.81     | 0.69      | 0.57   | 0.62     |
| Random Forest       | 0.80     | 0.67      | 0.54   | 0.60     |

The Logistic Regression model achieved slightly better performance compared to Random Forest. Visualizations such as confusion matrix and ROC curve were also generated to analyze model performance.

---

# Limitation

The project has certain limitations. The dataset used may not fully represent real-world customer behavior. The performance of the models depends on data quality and available features. Only two classification algorithms were implemented, and advanced techniques such as hyperparameter tuning and deep learning were not explored. The dataset may also contain class imbalance, which can affect prediction accuracy.

---

# Future Scope

Future improvements for this project may include:

* Implementing advanced algorithms such as XGBoost and Neural Networks
* Applying hyperparameter tuning techniques
* Using feature selection methods
* Handling class imbalance using SMOTE
* Deploying the model as a web application
* Using real-time customer data for prediction

---

# Conclusion

This project successfully implemented supervised machine learning techniques for customer churn prediction. Data preprocessing, train-test split, cross-validation, and model evaluation were performed effectively. Logistic Regression and Random Forest models were compared using multiple evaluation metrics.

The results demonstrated that Logistic Regression achieved slightly better performance on the given dataset. The project provided practical understanding of machine learning workflows and classification model evaluation techniques.
