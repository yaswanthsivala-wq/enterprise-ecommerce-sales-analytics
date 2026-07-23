import pandas as pd
import os


def extract_data():

    data_path = "."

    print("Reading generated CSV files...")


    customers = pd.read_csv(
        os.path.join(
            data_path,
            "customers.csv"
        )
    )


    products = pd.read_csv(
        os.path.join(
            data_path,
            "products.csv"
        )
    )


    orders = pd.read_csv(
        os.path.join(
            data_path,
            "orders.csv"
        )
    )


    order_items = pd.read_csv(
        os.path.join(
            data_path,
            "order_items.csv"
        )
    )


    print("✅ Data extracted")

    print(
        "Customers:",
        len(customers)
    )

    print(
        "Products:",
        len(products)
    )

    print(
        "Orders:",
        len(orders)
    )

    print(
        "Order Items:",
        len(order_items)
    )


    return {
        "customers": customers,
        "products": products,
        "orders": orders,
        "order_items": order_items
    }



if __name__ == "__main__":

    extract_data()