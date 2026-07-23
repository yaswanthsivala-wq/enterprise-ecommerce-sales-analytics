import pandas as pd
from etl.extract import extract_data


def transform_data():

    data = extract_data()


    customers = data["customers"]
    products = data["products"]
    orders = data["orders"]
    order_items = data["order_items"]


    print("Starting data transformation...")


    # ======================================
    # CUSTOMERS TRANSFORMATION
    # ======================================

    customers = customers.drop_duplicates()

    customers = customers.fillna({
        "country": "Unknown"
    })


    customers["first_name"] = (
        customers["first_name"]
        .str.strip()
    )

    customers["last_name"] = (
        customers["last_name"]
        .str.strip()
    )

    customers["country"] = (
        customers["country"]
        .str.strip()
    )



    # ======================================
    # PRODUCTS TRANSFORMATION
    # ======================================

    products = products.drop_duplicates()


    products = products.fillna({
        "category": "Unknown",
        "inventory": 0
    })


    products["product_name"] = (
        products["product_name"]
        .str.strip()
    )


    products["category"] = (
        products["category"]
        .str.strip()
    )



    # ======================================
    # ORDERS TRANSFORMATION
    # ======================================

    orders = orders.drop_duplicates()


    orders["order_date"] = pd.to_datetime(
        orders["order_date"]
    )


    orders = orders.fillna({
        "status": "Unknown",
        "total_amount": 0
    })



    # ======================================
    # ORDER ITEMS TRANSFORMATION
    # ======================================

    order_items = order_items.drop_duplicates()


    order_items = order_items.fillna({
        "quantity": 0,
        "price": 0
    })


    print("✅ Data transformation completed")


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

    transform_data()