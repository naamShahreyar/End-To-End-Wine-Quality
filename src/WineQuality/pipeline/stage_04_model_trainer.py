from WineQuality import logger
from WineQuality.config.configuration import ConfigurationManager
from WineQuality.components.model_trainer import ModelTrainer

STAGE_NAME = "Model Trainer Stage"

class ModelTrainingPipeline:
    
        def __init__(self):
            pass
    
        def main(self):
            config = ConfigurationManager()
            model_trainer_configs = config.get_model_trainer_configs()
            for model_trainer_config in model_trainer_configs:
                model_trainer = ModelTrainer(config=model_trainer_config)
                model_trainer.train_model()