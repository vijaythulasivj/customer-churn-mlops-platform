from src.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
)

from src.utils import read_yaml


class ConfigurationManager:

    def __init__(self):

        self.config = read_yaml("config/config.yaml")

        self.params = read_yaml("config/params.yaml")

    def get_data_ingestion_config(self):

        config = self.config["data_ingestion"]

        return DataIngestionConfig(
            source_data_path=config["source_data_path"],
            raw_data_path=config["raw_data_path"]
        )

    def get_data_validation_config(self):

        config = self.config["data_validation"]

        return DataValidationConfig(
            validated_data_path=config["validated_data_path"]
        )

    def get_data_transformation_config(self):

        config = self.config["data_transformation"]

        return DataTransformationConfig(
            train_data_path=config["train_data_path"],
            test_data_path=config["test_data_path"]
        )

    def get_model_trainer_config(self):

        config = self.config["model_trainer"]
        params = self.params["model"]

        return ModelTrainerConfig(
            model_path=config["model_path"],
            n_estimators=params["n_estimators"],
            random_state=params["random_state"]
        )
