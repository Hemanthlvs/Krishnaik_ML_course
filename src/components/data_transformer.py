import pandas as pd
import numpy as np
import os

from dataclasses import dataclass
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from src.utils import save_obj
from src.logger import logging
from src.exception import CustomException

@dataclass
class data_transform_config():
    tranformed_data = os.path.join('artifacts', 'transformed.pkl')

class transformer():
    def __init__(self):
        self.datatransformconfig = data_transform_config()


    def initiate_data_transform(self, train_path, test_path):
        logging.info("transformation initialised........")
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            numeric_cols = train_df.select_dtypes(exclude=object).columns
            # Convert to a list and exclude 'column_21'
            numeric_cols = [col for col in numeric_cols if col != 'math_score']

            # Convert back to Index object
            numeric_cols = pd.Index(numeric_cols)

            cat_cols = train_df.select_dtypes(include=object).columns

            num_pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy='most_frequent')),
                    ("onehotencoder", OneHotEncoder())
                ]
            )
            
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline",  num_pipeline,numeric_cols),
                    ("cat_pipeline", cat_pipeline,cat_cols)
                ]
            )

            train_input_df = train_df.drop(columns=["math_score"],axis=1)
            train_output_df = train_df["math_score"]
            test_input_df = test_df.drop(columns=["math_score"],axis=1)
            test_output_df = test_df["math_score"]

            train_input_array = preprocessor.fit_transform(train_input_df)
            test_input_array = preprocessor.transform(test_input_df)

            logging.info("data got standardised")

            train_arr = np.c_[train_input_array,np.array(train_output_df)]
            test_arr = np.c_[test_input_array, np.array(test_output_df)]

            save_obj(self.datatransformconfig.tranformed_data, preprocessor)
            logging.info("transform.pkl object got created")

            return train_arr, test_arr, self.datatransformconfig.tranformed_data
        
        except Exception as e:
            raise CustomException
        
    



