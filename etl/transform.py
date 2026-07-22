import pandas as pd
from etl.extract import extract_data


def transform_data():

    df = extract_data()

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna({
        "status": "Unknown",
        "country": "Unknown"
    })

    # Convert date
    df["order_date"] = pd.to_datetime(
    df["order_date"],
    format="mixed"
)

    # Create revenue column
    df["total_amount"] = (
        df["price"] * df["quantity"]
    )

    # Clean text columns
    df["category"] = df["category"].str.strip()
    df["country"] = df["country"].str.strip()

    print("✅ Data transformation completed")
    print(df.head())

    return df


if __name__ == "__main__":
    transform_data()