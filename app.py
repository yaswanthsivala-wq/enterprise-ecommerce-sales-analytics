import streamlit as st

from dashboard.pages.executive_dashboard import show_executive
from dashboard.pages.sales_dashboard import show_sales
from dashboard.pages.customer_dashboard import show_customer
from dashboard.pages.product_dashboard import show_product


st.set_page_config(
    page_title="Enterprise Ecommerce Analytics",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "Select Dashboard",
    [
        "Executive Dashboard",
        "Sales Dashboard",
        "Customer Dashboard",
        "Product Dashboard"
    ]
)

if page == "Executive Dashboard":
    show_executive()

elif page == "Sales Dashboard":
    show_sales()

elif page == "Customer Dashboard":
    show_customer()

elif page == "Product Dashboard":
    show_product()