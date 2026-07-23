import streamlit as st
import plotly.express as px

from utils.queries import (
    get_category_sales,
    get_top_products,
    get_product_kpis
)


def show_product():

    st.title("📦 Product Analytics Dashboard")

    st.markdown(
        "### Enterprise E-Commerce Product Performance"
    )


    # =====================================
    # SIDEBAR FILTERS
    # =====================================

    st.sidebar.header(
        "🔎 Product Filters"
    )


    category_data = get_category_sales()


    category_filter = st.sidebar.selectbox(
        "📦 Category",
        [
            "All"
        ]
        +
        category_data["category"].tolist()
    )


    # =====================================
    # KPI CARDS
    # =====================================


    kpi = get_product_kpis().iloc[0]


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "📦 Total Products",
            f"{int(kpi['total_products']):,}"
        )


    with col2:

        st.metric(
            "📈 Units Sold",
            f"{int(kpi['units_sold']):,}"
        )


    with col3:

        st.metric(
            "💰 Product Revenue",
            f"${kpi['total_revenue']:,.2f}"
        )


    st.divider()



    # =====================================
    # TOP PRODUCTS
    # =====================================


    st.subheader(
        "🏆 Top Products by Revenue"
    )


    products = get_top_products()


    if category_filter != "All":

        products = products[
            products["category"]
            ==
            category_filter
        ]


    fig = px.bar(

        products,

        x="revenue",

        y="product_name",

        orientation="h",

        title="Highest Revenue Products"

    )


    fig.update_layout(

        yaxis={
            "categoryorder":
            "total ascending"
        }

    )


    st.plotly_chart(
        fig,
        width="stretch"
    )



    st.divider()



    # =====================================
    # CATEGORY ANALYSIS
    # =====================================


    st.subheader(
        "📊 Revenue by Category"
    )


    category_sales = get_category_sales()


    fig2 = px.pie(

        category_sales,

        names="category",

        values="revenue",

        hole=0.45,

        title="Category Revenue Contribution"

    )


    st.plotly_chart(
        fig2,
        width="stretch"
    )



    st.divider()



    # =====================================
    # UNITS SOLD ANALYSIS
    # =====================================


    st.subheader(
        "📈 Units Sold by Category"
    )


    fig3 = px.bar(

        category_sales,

        x="category",

        y="units_sold",

        title="Product Volume Performance"

    )


    st.plotly_chart(
        fig3,
        width="stretch"
    )



    st.divider()



    # =====================================
    # PRODUCT TABLE
    # =====================================


    st.subheader(
        "📋 Product Performance Details"
    )


    st.dataframe(

        products,

        width="stretch"

    )
    
    