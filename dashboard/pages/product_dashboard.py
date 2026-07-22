import streamlit as st
import plotly.express as px

from utils.queries import get_category_sales


def show_product():

    st.title("📦 Product Dashboard")

    products = get_category_sales()

    if products.empty:
        st.warning("No product data available")
        return

    fig = px.pie(
        products,
        names="category",
        values="revenue",
        title="Revenue by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Category Sales Details")

    st.dataframe(
        products,
        use_container_width=True
    )