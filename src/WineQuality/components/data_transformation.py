import os
import pandas as pd
from WineQuality import logger
from sklearn.model_selection import train_test_split
from WineQuality.entity.config_entity import DataTransformationConfig

class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def train_test_spliting_data(self):

        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info(f"train and test data saved at {self.config.root_dir}")
        logger.info(f"train shape: {train.shape}, test shape: {test.shape}")
        
