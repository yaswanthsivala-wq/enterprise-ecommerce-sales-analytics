import streamlit as st

from dashboard.pages.home_dashboard import show_home


st.set_page_config(
    page_title="Enterprise Ecommerce Analytics",
    page_icon="📊",
    layout="wide"
)


st.sidebar.title("📊 Navigation")


page = st.sidebar.radio(
    "Select Dashboard",
    [
        "Home",
        "Sales Dashboard",
        "Customer Dashboard",
        "Product Dashboard"
    ]
)



if page == "Home":

    show_home()



elif page == "Sales Dashboard":

    from dashboard.pages.sales_dashboard import show_sales

    show_sales()



elif page == "Customer Dashboard":

    from dashboard.pages.customer_dashboard import show_customer

    show_customer()



elif page == "Product Dashboard":

    from dashboard.pages.product_dashboard import show_product

    show_product()