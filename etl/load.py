import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from sqlalchemy.orm import Session

from database import SessionLocal
from models import Customer, Product, Order, OrderItem
from etl.transform import transform_data


def load_data():

    print("Starting optimized data load...")

    # Get transformed data
    df = transform_data()

    print(f"Total records: {len(df)}")


    db: Session = SessionLocal()


    try:


        # ==========================================
        # CUSTOMERS
        # ==========================================

        customer_df = df.drop_duplicates(
            subset=["customer_id"]
        ).copy()


        # Fix duplicate emails
        customer_df["email"] = (
            customer_df["email"]
            .str.lower()
            + "_"
            + customer_df["customer_id"].astype(str)
        )


        customers = []


        for _, row in customer_df.iterrows():

            customers.append(
                Customer(
                    customer_id=int(row["customer_id"]),
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    email=row["email"],
                    country=row["country"]
                )
            )


        db.bulk_save_objects(customers)

        print(
            f"✅ Customers loaded: {len(customers)}"
        )



        # ==========================================
        # PRODUCTS
        # ==========================================

        product_df = df.drop_duplicates(
            subset=["product_id"]
        )


        products = []


        for _, row in product_df.iterrows():

            products.append(
                Product(
                    product_id=int(row["product_id"]),
                    product_name=row["product_name"],
                    category=row["category"],
                    price=float(row["price"]),
                    inventory=0
                )
            )


        db.bulk_save_objects(products)


        print(
            f"✅ Products loaded: {len(products)}"
        )



        # ==========================================
        # ORDERS
        # ==========================================

        orders = []


        for index, row in df.iterrows():

            orders.append(
                Order(
                    order_id=index + 1,
                    customer_id=int(row["customer_id"]),
                    order_date=row["order_date"],
                    total_amount=float(row["total_amount"]),
                    status=row["status"]
                )
            )


        db.bulk_save_objects(orders)


        print(
            f"✅ Orders loaded: {len(orders)}"
        )



        # ==========================================
        # ORDER ITEMS
        # ==========================================

        order_items = []


        for index, row in df.iterrows():

            order_items.append(
                OrderItem(
                    order_item_id=index + 1,
                    order_id=index + 1,
                    product_id=int(row["product_id"]),
                    quantity=int(row["quantity"]),
                    price=float(row["price"])
                )
            )


        db.bulk_save_objects(order_items)


        print(
            f"✅ Order Items loaded: {len(order_items)}"
        )



        # Commit all changes

        db.commit()


        print(
            "🎉 All data loaded successfully into Supabase!"
        )


    except Exception as e:


        db.rollback()

        print(
            "❌ Load failed"
        )

        print(e)



    finally:

        db.close()



if __name__ == "__main__":
    load_data()