from src.configuration.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion


def main():

    print("=" * 60)
    print("Customer Churn MLOps Platform")
    print("=" * 60)

    config = ConfigurationManager()

    ingestion_config = config.get_data_ingestion_config()

    ingestion = DataIngestion(ingestion_config)

    ingestion.initiate_data_ingestion()

    print("\nData Ingestion Completed Successfully")


if __name__ == "__main__":
    main()
