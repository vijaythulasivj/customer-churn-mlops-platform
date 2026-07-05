from src.configuration.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_evaluation import ModelEvaluation


class TrainingPipeline:

    def start_pipeline(self):

        config = ConfigurationManager()

        # -------------------------
        # Data Ingestion
        # -------------------------
        ingestion = DataIngestion(
            config.get_data_ingestion_config()
        )

        raw_data = ingestion.initiate_data_ingestion()


        # -------------------------
        # Data Validation
        # -------------------------
        validation = DataValidation(
            config.get_data_validation_config()
        )

        validated_data = validation.initiate_data_validation(
            raw_data
        )

        # -------------------------
        # Data Transformation
        # -------------------------
        transformation = DataTransformation(
            config.get_data_transformation_config()
        )

        train_data, test_data = transformation.initiate_data_transformation(
            validated_data
        ) 
        # -------------------------
        # Model Training
        # -------------------------
        trainer = ModelTrainer(
            config.get_model_trainer_config()
        )
        model_path = trainer.initiate_model_training(
            train_data
        )
        # -------------------------
        # Model Evaluation
        # -------------------------
        evaluation = ModelEvaluation()

        evaluation.initiate_model_evaluation(
            model_path,
            test_data
        )

           
