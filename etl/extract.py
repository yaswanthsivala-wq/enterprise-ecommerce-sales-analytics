import pandas as pd


def extract_data():

    file_path = "data/ecommerce_sales.csv"

    df = pd.read_csv(file_path)

    print("✅ Data extracted")
    print(df.head())

    return df


if __name__ == "__main__":
    extract_data()