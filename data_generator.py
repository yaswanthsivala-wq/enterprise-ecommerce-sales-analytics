import pandas as pd
import random
import os
from faker import Faker
from datetime import datetime, timedelta


fake = Faker()

FILE = "data/ecommerce_sales.csv"

NEW_RECORDS = 1000


countries = [
    "USA",
    "Canada",
    "UK",
    "Germany",
    "Australia"
]


products = [
    (101, "Laptop", "Electronics", 1200),
    (102, "Phone", "Electronics", 800),
    (103, "Headphones", "Accessories", 150),
    (104, "Keyboard", "Accessories", 90),
    (105, "Monitor", "Electronics", 400),
    (106, "Mouse", "Accessories", 50),
    (107, "Tablet", "Electronics", 600),
    (108, "Charger", "Accessories", 40)
]


statuses = [
    "Completed",
    "Pending",
    "Cancelled"
]


def generate_sales():

    sales = []


    start_id = 1


    if os.path.exists(FILE):

        old = pd.read_csv(FILE)

        start_id = old["customer_id"].max() + 1


    for i in range(
        start_id,
        start_id + NEW_RECORDS
    ):

        product = random.choice(products)


        quantity = random.randint(1,5)


        sales.append({

            "customer_id": i,

            "first_name":
                fake.first_name(),

            "last_name":
                fake.last_name(),

            "email":
                fake.email(),

            "country":
                random.choice(countries),

            "product_id":
                product[0],

            "product_name":
                product[1],

            "category":
                product[2],

            "price":
                product[3],

            "quantity":
                quantity,

            "order_date":
                datetime.now()
                -
                timedelta(
                    days=random.randint(0,365)
                ),

            "status":
                random.choice(statuses)

        })


    new_data = pd.DataFrame(sales)


    if os.path.exists(FILE):

        old = pd.read_csv(FILE)

        final = pd.concat(
            [old,new_data],
            ignore_index=True
        )

    else:

        final = new_data


    final.to_csv(
        FILE,
        index=False
    )


    print(
        "✅ Added",
        NEW_RECORDS,
        "new sales records"
    )

    print(
        "Total rows:",
        len(final)
    )


if __name__ == "__main__":

    generate_sales()