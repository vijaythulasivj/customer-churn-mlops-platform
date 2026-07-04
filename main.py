from src.ingestion import load_data
from src.validation import validate_data
from src.preprocessing import preprocess
from src.train import train_model
from src.evaluate import evaluate


def main():

    print("=" * 60)
    print(" Customer Churn MLOps Pipeline ")
    print("=" * 60)

    # Step 1 - Load Data
    df = load_data()

    # Step 2 - Validate Data
    df = validate_data(df)

    # Step 3 - Preprocess Data
    X_train, X_test, y_train, y_test = preprocess(df)

    # Step 4 - Train Model
    model = train_model(X_train, y_train)

    # Step 5 - Evaluate Model
    evaluate(model, X_test, y_test)

    print("\nPipeline Completed Successfully")


if __name__ == "__main__":
    main()













