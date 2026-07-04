from src.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
)


class ConfigurationManager:

    def get_data_ingestion_config(self):
        return DataIngestionConfig()

    def get_data_validation_config(self):
        return DataValidationConfig()

    def get_data_transformation_config(self):
        return DataTransformationConfig()

    def get_model_trainer_config(self):
        return ModelTrainerConfig()
