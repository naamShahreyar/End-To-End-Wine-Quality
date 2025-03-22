import os
import pandas as pd
import urllib.request as request
import zipfile
from WineQuality import logger
from WineQuality.utils.common import get_size
from WineQuality.entity.config_entity import DataValidationConfig


class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:

        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)

            column_info = dict(data.dtypes)

            all_schema = self.config.all_schema

            for col, dtype in column_info.items():
                expected_dtype = all_schema.get(col, None)

                if expected_dtype is None:
                    logger.error(f"Column {col} not in schema")
                    validation_status = False
                    break

                else:
                    if str(dtype) != str(expected_dtype):
                        logger.error(f"Column {col} dtype mismatch")
                        validation_status = False
                        break
            
            # Write final validation status to file
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation Status: {validation_status}")
                
            return validation_status
        
        except Exception as e:
            raise e


                    
                

        
        