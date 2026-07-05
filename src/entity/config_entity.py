from dataclasses import dataclass


@dataclass
class DataIngestionConfig:

    raw_data_path: str = "artifacts/raw/customer_churn.csv"


@dataclass
class DataValidationConfig:

    validation_path: str = "artifacts/validated/"


@dataclass
class DataTransformationConfig:

    transformed_path: str = "artifacts/transformed/"


@dataclass
class ModelTrainerConfig:

    model_path: str = "models/model.pkl"
