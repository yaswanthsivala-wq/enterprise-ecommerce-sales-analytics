import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from sqlalchemy.orm import Session

from database import SessionLocal
from models import Customer, Product, Order, OrderItem

from etl.transform import transform_data



def load_data():

    print("Starting optimized data load...")


    # ==========================================
    # TRANSFORM DATA
    # ==========================================

    data = transform_data()


    customer_df = data["customers"]
    product_df = data["products"]
    order_df = data["orders"]
    order_item_df = data["order_items"]


    print("Total records:")
    print(f"Customers: {len(customer_df)}")
    print(f"Products: {len(product_df)}")
    print(f"Orders: {len(order_df)}")
    print(f"Order Items: {len(order_item_df)}")


    db: Session = SessionLocal()


    try:


        # ==========================================
        # CUSTOMERS
        # ==========================================

        print("Loading customers...")


        customers = []


        for _, row in customer_df.iterrows():

            customers.append(
                Customer(
                    customer_id=int(row["customer_id"]),
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    email=str(row["email"]).lower(),
                    country=row["country"]
                )
            )


        db.bulk_save_objects(customers)

        db.commit()


        print(
            f"✅ Customers loaded: {len(customers)}"
        )



        # ==========================================
        # PRODUCTS
        # ==========================================


        print("Loading products...")


        products = []


        for _, row in product_df.iterrows():

            products.append(
                Product(
                    product_id=int(row["product_id"]),
                    product_name=row["product_name"],
                    category=row["category"],
                    price=float(row["price"]),
                    inventory=int(
                        row.get("inventory",0)
                    )
                )
            )


        db.bulk_save_objects(products)

        db.commit()


        print(
            f"✅ Products loaded: {len(products)}"
        )



        # ==========================================
        # ORDERS
        # ==========================================


        print("Loading orders...")


        orders = []


        for _, row in order_df.iterrows():

            orders.append(
                Order(
                    order_id=int(row["order_id"]),
                    customer_id=int(row["customer_id"]),
                    order_date=row["order_date"],
                    total_amount=float(row["total_amount"]),
                    status=row["status"]
                )
            )


        db.bulk_save_objects(
            orders
        )

        db.commit()


        print(
            f"✅ Orders loaded: {len(orders)}"
        )



        # ==========================================
        # ORDER ITEMS
        # ==========================================


        print("Loading order items...")


        order_items = []


        for _, row in order_item_df.iterrows():

            order_items.append(
                OrderItem(
                    order_item_id=int(row["order_item_id"]),
                    order_id=int(row["order_id"]),
                    product_id=int(row["product_id"]),
                    quantity=int(row["quantity"]),
                    price=float(row["price"])
                )
            )


        db.bulk_save_objects(
            order_items
        )


        db.commit()


        print(
            f"✅ Order Items loaded: {len(order_items)}"
        )



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