import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random


fake = Faker()

np.random.seed(42)
random.seed(42)


# ==========================================
# CONFIGURATION
# ==========================================

CUSTOMERS = 10000
PRODUCTS = 500
ORDERS = 50000


# ==========================================
# GENERATE CUSTOMERS
# ==========================================

def generate_customers():

    countries = [
        "USA",
        "Canada",
        "UK",
        "Germany",
        "France",
        "India",
        "Australia",
        "Japan"
    ]

    customers = []

    for i in range(1, CUSTOMERS + 1):

        customers.append({

            "customer_id": i,

            "first_name": fake.first_name(),

            "last_name": fake.last_name(),

            "email": fake.unique.email(),

            "country": random.choice(countries),

            "created_at":
                fake.date_time_between(
                    start_date="-5y",
                    end_date="now"
                )

        })


    return pd.DataFrame(customers)



# ==========================================
# GENERATE PRODUCTS
# ==========================================

def generate_products():

    categories = {

        "Electronics": [
            "Laptop",
            "Smartphone",
            "Headphones",
            "Camera"
        ],

        "Clothing": [
            "Shirt",
            "Jeans",
            "Jacket",
            "Shoes"
        ],

        "Home": [
            "Chair",
            "Table",
            "Lamp",
            "Sofa"
        ],

        "Beauty": [
            "Perfume",
            "Cream",
            "Makeup"
        ],

        "Sports": [
            "Football",
            "Equipment",
            "Fitness Gear"
        ],

        "Books": [
            "Novel",
            "Textbook",
            "Magazine"
        ]

    }


    products=[]


    for i in range(1, PRODUCTS+1):

        category=random.choice(
            list(categories.keys())
        )


        products.append({

            "product_id": i,

            "product_name":
                random.choice(
                    categories[category]
                )
                +
                " "
                +
                fake.word().title(),

            "category": category,

            "price":
                round(
                    random.uniform(
                        10,
                        2000
                    ),
                    2
                ),

            "inventory":
                random.randint(
                    50,
                    1000
                )

        })


    return pd.DataFrame(products)



# ==========================================
# GENERATE ORDERS
# ==========================================

def generate_orders():

    statuses = [
        "Completed",
        "Completed",
        "Completed",
        "Pending",
        "Cancelled"
    ]


    orders=[]


    start_date = datetime(2023,1,1)


    for i in range(1, ORDERS+1):

        orders.append({

            "order_id": i,

            "customer_id":
                random.randint(
                    1,
                    CUSTOMERS
                ),

            "order_date":
                start_date +
                timedelta(
                    days=random.randint(
                        0,
                        1300
                    )
                ),

            "total_amount": 0,

            "status":
                random.choice(
                    statuses
                )

        })


    return pd.DataFrame(orders)



# ==========================================
# GENERATE ORDER ITEMS
# ==========================================

def generate_order_items(products):

    items=[]

    item_id=1


    for order_id in range(
        1,
        ORDERS+1
    ):

        number_of_items=random.randint(
            1,
            5
        )


        for _ in range(number_of_items):


            product = products.sample(
                1
            ).iloc[0]


            items.append({

                "order_item_id":
                    item_id,

                "order_id":
                    order_id,

                "product_id":
                    int(
                        product.product_id
                    ),

                "quantity":
                    random.randint(
                        1,
                        5
                    ),

                "price":
                    float(
                        product.price
                    )

            })


            item_id += 1


    return pd.DataFrame(items)



# ==========================================
# MAIN EXECUTION
# ==========================================

if __name__ == "__main__":


    print("Generating customers...")
    customers = generate_customers()


    print("Generating products...")
    products = generate_products()


    print("Generating orders...")
    orders = generate_orders()


    print("Generating order items...")
    order_items = generate_order_items(
        products
    )


    # Calculate order totals

    revenue = (
        order_items
        .assign(
            amount=lambda x:
            x.quantity * x.price
        )
        .groupby("order_id")
        ["amount"]
        .sum()
    )


    orders["total_amount"] = (
        orders["order_id"]
        .map(revenue)
    )



    # Save files

    customers.to_csv(
        "customers.csv",
        index=False
    )


    products.to_csv(
        "products.csv",
        index=False
    )


    orders.to_csv(
        "orders.csv",
        index=False
    )


    order_items.to_csv(
        "order_items.csv",
        index=False
    )



    print("==============================")
    print("DATA GENERATION COMPLETE")
    print("==============================")


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