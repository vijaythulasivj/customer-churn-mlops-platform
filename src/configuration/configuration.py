from src.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    MLflowConfig
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


        return DataTransformationConfig(
            train_data_path=self.config["data_transformation"]["train_data_path"],
            test_data_path=self.config["data_transformation"]["test_data_path"],
            preprocessor_path=self.config["data_transformation"]["preprocessor_path"],
            test_size=self.params["training"]["test_size"]
        )
       

    def get_model_trainer_config(self):

                
        return ModelTrainerConfig(
            model_path=self.config["model_trainer"]["model_path"],
            n_estimators=self.params["model"]["n_estimators"],
            random_state=self.params["model"]["random_state"]
        )

    def get_mlflow_config(self):

        return MLflowConfig(
            experiment_name=self.config["mlflow"]["experiment_name"]
        )
