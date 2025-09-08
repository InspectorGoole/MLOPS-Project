import os
from mlproject import logger 
from mlproject.entity.config_entity import DataValidationConfig
import pandas as pd 

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir) # it will read your csv file
            all_cols = list(data.columns) # then list down all the columns

            all_schema = self.config.all_schema.keys() #  then it will check with schema to see if all the columns are present

            for col in all_cols:
                if col not in all_schema:  # if columns are missing it will return status as false
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation status: {validation_status}')
                else:
                    validation_status = True # otherwise it will return status as true
                    with open (self.config.STATUS_FILE, 'w') as f:
                        f.write(f'validation status: {validation_status}')

            return validation_status
        
        except Exception as e:
            raise e 


