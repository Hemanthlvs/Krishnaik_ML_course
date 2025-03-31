import pandas as pd
import os
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformer import transformer
from src.components.model_training import model_training

from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class path_config:
    raw_path = os.path.join('artifacts', 'raw_data.csv')
    test_path = os.path.join('artifacts', 'test_data.csv')
    train_path = os.path.join('artifacts', 'train_data.csv')

class ingestion:
    def __init__(self):
        self.ingestion_paths = path_config()

    def initiate_ingestion(self):
        logging.info("Ingestion started...........")

        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Dataframe Created")
            os.makedirs(os.path.dirname(self.ingestion_paths.raw_path),exist_ok=True)
            logging.info("Artifacts folder created")
            df.to_csv(self.ingestion_paths.raw_path,index=False, header=True)
            logging.info("raw file created")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_paths.train_path,index=False, header=True)
            logging.info("training file created")
            test_set.to_csv(self.ingestion_paths.test_path,index=False, header=True)
            logging.info("testing file created")

            return (self.ingestion_paths.raw_path,
                    self.ingestion_paths.train_path,
                    self.ingestion_paths.test_path
                    )
        except Exception as e:
            raise CustomException

if __name__ == "__main__":
    ingestor = ingestion()
    _,train_path,test_path = ingestor.initiate_ingestion() 

    transformer = transformer()
    train_arr, test_arr, transformer_pkl = transformer.initiate_data_transform(train_path,test_path)
    
    model_training = model_training()
    r2_score = model_training.initiate_model_training(train_arr, test_arr)
    print(r2_score)



