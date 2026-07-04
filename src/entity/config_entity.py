from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    raw_data_path: str = "data/raw/customer_churn.csv"


@dataclass
class DataValidationConfig:
    validated_data_path: str = "data/processed/validated.csv"


@dataclass
class DataTransformationConfig:
    train_data_path: str = "data/processed/train.csv"
    test_data_path: str = "data/processed/test.csv"


@dataclass
class ModelTrainerConfig:
    model_path: str = "models/model.pkl"
