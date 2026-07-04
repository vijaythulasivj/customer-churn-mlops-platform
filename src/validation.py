def validate_data(df):

    print("\nValidating Dataset...\n")

    print("Missing Values")

    print(df.isnull().sum())

    print("\nDuplicate Rows")

    print(df.duplicated().sum())

    if df.isnull().sum().sum() > 0:

        raise Exception("Dataset contains missing values")

    print("\nValidation Successful")

    return df
