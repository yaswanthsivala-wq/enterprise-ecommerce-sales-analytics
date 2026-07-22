import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from database import engine
import pandas as pd


def top_customers():

    query = """
    SELECT
        c.customer_id,
        c.first_name,
        c.last_name,
        c.country,
        SUM(o.total_amount) AS total_spent
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    GROUP BY
        c.customer_id,
        c.first_name,
        c.last_name,
        c.country
    ORDER BY total_spent DESC;
    """

    df = pd.read_sql(query, engine)

    print("\n👥 Top Customers")
    print(df)

    return df



def country_sales():

    query = """
    SELECT
        c.country,
        SUM(o.total_amount) AS revenue
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    GROUP BY c.country
    ORDER BY revenue DESC;
    """

    df = pd.read_sql(query, engine)

    print("\n🌎 Sales By Country")
    print(df)

    return df



if __name__ == "__main__":

    top_customers()
    country_sales()