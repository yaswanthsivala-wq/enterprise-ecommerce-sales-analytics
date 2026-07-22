from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    country = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship("Order", back_populates="customer")


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    category = Column(String)
    price = Column(Float)
    inventory = Column(Integer)

    order_items = relationship("OrderItem", back_populates="product")


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    customer_id = Column(
        Integer,
        ForeignKey("customers.customer_id")
    )

    order_date = Column(DateTime)
    total_amount = Column(Float)
    status = Column(String)

    customer = relationship(
        "Customer",
        back_populates="orders"
    )

    order_items = relationship(
        "OrderItem",
        back_populates="order"
    )


class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id = Column(Integer, primary_key=True)

    order_id = Column(
        Integer,
        ForeignKey("orders.order_id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.product_id")
    )

    quantity = Column(Integer)
    price = Column(Float)

    order = relationship(
        "Order",
        back_populates="order_items"
    )

    product = relationship(
        "Product",
        back_populates="order_items"
    )