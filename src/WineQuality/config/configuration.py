from WineQuality.constants import *
from WineQuality.utils.common import read_yaml, create_directories
from WineQuality.entity.config_entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig)

class ConfigurationManager:
    
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH,schema_filepath = SCHEMA_FILE_PATH):
        
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
       
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            unzip_data_dir = config.unzip_data_dir,
            STATUS_FILE = config.STATUS_FILE,
            all_schema = schema
        )
       
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            
        )
       
        return data_transformation_config
    
    def get_model_trainer_configs(self) -> list[ModelTrainerConfig]:

        config = self.config.model_trainer
        params = self.params
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_configs =[]

        for model_name, params_grid in params.items():
            model_trainer_config = ModelTrainerConfig(
                root_dir= config.root_dir,
                model_name= model_name,
                params_grid= params_grid,
                train_data_path= config.train_data_path,
                model_save_dir= config.model_save_dir,
                target_column= schema.name

            )

            model_trainer_configs.append(model_trainer_config)

        return model_trainer_configs