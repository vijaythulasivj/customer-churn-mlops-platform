from src.pipeline.training_pipeline import TrainingPipeline


def main():

    print("=" * 60)
    print("Customer Churn MLOps Platform")
    print("=" * 60)

    pipeline = TrainingPipeline()

    pipeline.start_pipeline()

    print("\nPipeline Executed Successfully")


if __name__ == "__main__":
    main()
