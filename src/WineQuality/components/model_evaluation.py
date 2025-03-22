import os
import pandas as pd
from WineQuality import logger
import json
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pickle
from WineQuality.entity.config_entity import ModelEvaluationConfig



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate_model(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop(columns=[self.config.target_column])
        train_y = train_data[self.config.target_column]

        test_x = test_data.drop(columns=[self.config.target_column])
        test_y = test_data[self.config.target_column]

        logger.info(f"Evaluating {self.config.model_name} model")

        # Load the model
        with open(self.config.model_path, "rb") as f:
            trained_model = pickle.load(f)

        y_pred_train = trained_model.predict(train_x)
        y_pred_test = trained_model.predict(test_x)

        train_metrics = self.calculate_metrics(train_y, y_pred_train)
        test_metrics = self.calculate_metrics(test_y, y_pred_test)

          # Define paths
        train_metric_save_path = os.path.join(self.config.evaluation_save_dir, self.config.model_name, f"{self.config.model_name}_train.json")
        test_metric_save_path = os.path.join(self.config.evaluation_save_dir, self.config.model_name, f"{self.config.model_name}_test.json")

        # Ensure the directories exist (fix: use os.path.dirname)
        os.makedirs(os.path.dirname(train_metric_save_path), exist_ok=True)
        os.makedirs(os.path.dirname(test_metric_save_path), exist_ok=True)

        with open(train_metric_save_path, 'w') as f:
            json.dump(train_metrics, f)

        with open(test_metric_save_path, 'w') as f:
            json.dump(test_metrics, f)

    def calculate_metrics(self, actual, predicted):

        mse = mean_squared_error(actual, predicted)
        mae = mean_absolute_error(actual, predicted)
        r2 = r2_score(actual, predicted)

        return {'MSE':mse,
                'MAE':mae,
                'R2':r2}

        