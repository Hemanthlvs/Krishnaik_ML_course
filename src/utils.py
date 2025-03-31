import os
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score
import pandas as pd

def save_obj(file_path, obj):
    try:
        directory = os.path.dirname(file_path)
        os.makedirs(directory,exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    
    except Exception as e:
        raise CustomException
    
# def evaluate_model(models, X_train, y_train, X_test, y_test):
    
#     report = {}

#     for i in range(len(list(models))):
#         model = list(models.values())[i]
#         model.fit(X_train, y_train)

#         y_train_pred = model.predict(X_train)
#         train_r2 = r2_score(y_train,y_train_pred)

#         y_test_pred = model.predict(X_test)
#         test_r2 =  r2_score(y_test, y_test_pred)

#         report[list(models.keys())[i]] = test_r2

#         return report


def load_path(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load()
        
    except Exception as e:
        raise CustomException
