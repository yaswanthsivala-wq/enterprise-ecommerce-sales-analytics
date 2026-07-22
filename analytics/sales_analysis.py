import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from database import engine
import pandas as pd


def get_sales_metrics():

    query = """
    SELECT
        COUNT(order_id) AS total_orders,
        SUM(total_amount) AS total_revenue,
        AVG(total_amount) AS average_order_value
    FROM orders;
    """

    df = pd.read_sql(query, engine)

    print("\n📊 Sales Metrics")
    print(df)

    return df



def get_order_status():

    query = """
    SELECT
        status,
        COUNT(order_id) AS total_orders,
        SUM(total_amount) AS revenue
    FROM orders
    GROUP BY status;
    """

    df = pd.read_sql(query, engine)

    print("\n📦 Order Status Analysis")
    print(df)

    return df



def get_monthly_sales():

    query = """
    SELECT
        DATE_TRUNC('month', order_date) AS month,
        SUM(total_amount) AS revenue
    FROM orders
    GROUP BY month
    ORDER BY month;
    """

    df = pd.read_sql(query, engine)

    print("\n📈 Monthly Sales Trend")
    print(df)

    return df



if __name__ == "__main__":

    get_sales_metrics()

    get_order_status()

    get_monthly_sales()