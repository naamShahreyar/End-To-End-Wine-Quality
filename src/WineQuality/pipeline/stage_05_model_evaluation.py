from WineQuality import logger
from WineQuality.config.configuration import ConfigurationManager
from WineQuality.components.model_evaluation import ModelEvaluation

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
        
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_configs = config.get_model_evaluation_configs()
        for model_evaluation_config in model_evaluation_configs:
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.evaluate_model()