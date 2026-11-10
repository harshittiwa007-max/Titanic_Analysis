# Titanic Survival Prediction


## Project Overview
This project uses Machine Learning to predict whether a passenger survived the Titanic disaster based on passenger information.

## Dataset
- Training data: 891 rows
- Testing data: 418 rows
- Target variable: `Survived`

## Features Used
- Pclass
- Sex
- Age
- SibSp
- Parch
- Fare
- Embarked

## Machine Learning Models
Four classification algorithms were trained and compared:

1. Logistic Regression
2. Decision Tree
3. K-Nearest Neighbors (KNN)
4. Gaussian Naive Bayes

## Model Evaluation
Models were evaluated using:
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Matthews Correlation Coefficient (MCC)
- 5-Fold Cross Validation

KNN achieved the best results among the four models in the current validation and cross-validation experiments.

## Best Model
K-Nearest Neighbors (KNN)

The trained model is saved as `best_model.joblib`.

## Project Structure
```text
Titanic_Analysis/
├── titanic_model/
│   ├── best_model.joblib
│   ├── knn.joblib
│   ├── logistic_regression.joblib
│   ├── decision_tree.joblib
│   ├── naive_bayes.joblib
│   ├── metrics_comparison.csv
│   └── validation_data.csv
├── app.py
└── requirements.txt
```

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn
- Joblib

## Run Locally
Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Future Improvements
- Improve feature engineering
- Tune model hyperparameters
- Improve model performance
- Deploy the application online
