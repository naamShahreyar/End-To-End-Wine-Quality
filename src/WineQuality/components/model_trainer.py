import os
import pandas as pd
from WineQuality import logger
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import GridSearchCV
import json
from WineQuality.entity.config_entity import ModelTrainerConfig

import pickle


model_dict = {'Lasso': Lasso(random_state=42), 'Ridge': Ridge(random_state=42)}


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        train_data = pd.read_csv(self.config.train_data_path)
        X = train_data.drop(columns=[self.config.target_column])
        y = train_data[self.config.target_column]

        model = model_dict[self.config.model_name]

        logger.info(f"Training {self.config.model_name} model")

        grid = GridSearchCV(estimator=model, param_grid=self.config.params_grid.params_grid, cv=5, n_jobs=-1)

        grid.fit(X, y)

        logger.info(f"Best Score: {grid.best_score_}")
        logger.info(f"Best Parameters: {grid.best_params_}")

        # Define paths
        model_save_path = os.path.join(self.config.model_save_dir, self.config.model_name, f"{self.config.model_name}.pkl")
        best_parameters_save_path = os.path.join(self.config.model_save_dir, self.config.model_name, f"{self.config.model_name}_best_parameters.json")

        # Ensure the directories exist (fix: use os.path.dirname)
        os.makedirs(os.path.dirname(model_save_path), exist_ok=True)

        with open(model_save_path, 'wb') as f:
            pickle.dump(grid.best_estimator_, f)

        with open(best_parameters_save_path, 'w') as f:
            json.dump(grid.best_params_, f)

        logger.info(f"Model saved at: {model_save_path}")
