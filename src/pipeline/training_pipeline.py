from src.configuration.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion


class TrainingPipeline:

    def start_pipeline(self):

        config = ConfigurationManager()

        ingestion_config = config.get_data_ingestion_config()

        ingestion = DataIngestion(ingestion_config)

        ingestion.initiate_data_ingestion()
