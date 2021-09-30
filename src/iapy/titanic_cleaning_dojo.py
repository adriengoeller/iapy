#!/usr/bin/env python

from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def get_model():
    """Function for getting a Random Forest model

    """

    rf = RandomForestClassifier(n_estimators=100, random_state=0, max_features=2)
    
    return rf


def get_score(model, X, Y):
    """Function for displaying score (percent) for a model"""

    score = round(model.score(X, Y) *100,2)
    return score


def format_result_for_kaggle(X_test, model):
    """Function for formatting results to kaggle format"""

    result = pd.DataFrame(X_test['PassengerId'])
    p_test = model.predict(X_test)
    pred = pd.DataFrame(p_test, columns=['Survived'])
    result = result.join(pred)
    result.to_csv("./data/result.csv", columns=["PassengerId", "Survived"], index=False)

