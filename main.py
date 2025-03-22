from WineQuality import logger
from WineQuality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from WineQuality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from WineQuality.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline


STAGE_NAME = "Data Ingestion Stage" 

try:
    logger.info(f"Training {STAGE_NAME} has started")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"Training {STAGE_NAME} has completed")

except Exception as e:
    logger.exception(f"Error in {STAGE_NAME} - {str(e)}")
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"Training {STAGE_NAME} has started")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f"Training {STAGE_NAME} has completed")

except Exception as e:
    logger.exception(f"Error in {STAGE_NAME} - {str(e)}")
    raise e



STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"Training {STAGE_NAME} has started")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.main()
    logger.info(f"Training {STAGE_NAME} has completed")

except Exception as e:
    logger.exception(f"Error in {STAGE_NAME} - {str(e)}")   
    raise e
