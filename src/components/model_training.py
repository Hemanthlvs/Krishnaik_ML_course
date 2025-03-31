import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

import warnings
warnings.filterwarnings('ignore')

from src.utils import save_obj
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import RandomizedSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

@dataclass
class model_file_config:
    model_file_path = os.path.join('artifacts', 'model.pkl')

class model_training:
    def __init__(self):
        self.model_file_config = model_file_config()

    def initiate_model_training(self, train_arr, test_arr):
        try:
            logging.info("model initialised........")
            X_train, X_test, y_train, y_test = (train_arr[:,:-1], test_arr[:,:-1], train_arr[:,-1], test_arr[:,-1])

            models = {
                    "linear_regression" : LinearRegression(),
                    "ridge" : Ridge(),
                    "lasso" : Lasso(),
                    "KNN" : KNeighborsRegressor(),
                    "Decision_Tree" : DecisionTreeRegressor(),
                    "random_forest" : RandomForestRegressor(),
                    "Adaboost" : AdaBoostRegressor(),
                    "svr" : SVR(),
                    "xgboost" : XGBRegressor()
                }
            
            report = {}

            for i in range(len(list(models))):
                model = list(models.values())[i]
                model.fit(X_train, y_train)

                y_train_pred = model.predict(X_train)
                train_r2 = r2_score(y_train,y_train_pred)

                y_test_pred = model.predict(X_test)
                test_r2 =  r2_score(y_test, y_test_pred)

                report[list(models.keys())[i]] = test_r2
        
            best_model_score = max(report.values())
            best_model_name = max(report, key=report.get)
            
            # The key=report.get argument in the max() function allows us to find the model name
            # with the highest R² score from the report dictionary.
            # 
            # - report is a dictionary where keys are model names and values are their R² scores.
            # - report.get retrieves the R² score for each model name.
            # - max(report, key=report.get) finds the key (model name) with the maximum value (highest R² score).
            # 
            # Example:
            # If report = {"linear_regression": 0.85, "ridge": 0.88, "lasso": 0.82},
            # then max(report, key=report.get) returns "ridge" because it has the highest score (0.88).

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")
            logging.info("Best model found and the model is {}".format(best_model))

            save_obj(
                file_path = self.model_file_config.model_file_path,
                obj = best_model
            )
            logging.info("model.pkl object got created")
            pred_value = best_model.predict(X_test)
            r2 = r2_score(y_test, pred_value)

            return r2

        except Exception as e:
            raise CustomException