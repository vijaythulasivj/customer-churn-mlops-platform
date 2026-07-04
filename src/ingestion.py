import pandas as pd
from config import DATA_PATH

def load_data():
    print("=" * 50)
    print("Loading Dataset...")
    print("=" * 50)

    df = pd.read_csv(DATA_PATH)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    return df
