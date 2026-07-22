import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from database import engine
import pandas as pd


def best_selling_products():

    query = """
    SELECT
        p.product_id,
        p.product_name,
        p.category,
        SUM(oi.quantity) AS units_sold,
        SUM(oi.quantity * oi.price) AS revenue
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id
    GROUP BY
        p.product_id,
        p.product_name,
        p.category
    ORDER BY revenue DESC;
    """

    df = pd.read_sql(query, engine)

    print("\n🏆 Best Selling Products")
    print(df)

    return df



def category_performance():

    query = """
    SELECT
        p.category,
        SUM(oi.quantity) AS units_sold,
        SUM(oi.quantity * oi.price) AS revenue
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id
    GROUP BY p.category
    ORDER BY revenue DESC;
    """

    df = pd.read_sql(query, engine)

    print("\n📦 Category Performance")
    print(df)

    return df



if __name__ == "__main__":

    best_selling_products()

    category_performance()