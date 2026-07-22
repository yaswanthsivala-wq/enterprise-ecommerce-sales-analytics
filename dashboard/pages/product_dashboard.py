import streamlit as st
import plotly.express as px

from utils.queries import (
    get_category_sales,
    get_top_products,
    get_product_kpis
)


def show_product():

    st.title("📦 Product Analytics Dashboard")

    # ==========================
    # KPI Cards
    # ==========================

    kpi = get_product_kpis().iloc[0]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "📦 Total Products",
        f"{int(kpi['total_products'])}"
    )

    col2.metric(
        "📈 Units Sold",
        f"{int(kpi['units_sold']):,}"
    )

    col3.metric(
        "💰 Revenue",
        f"${kpi['total_revenue']:,.2f}"
    )

    st.divider()

    # ==========================
    # Top Products
    # ==========================

    st.subheader("🏆 Top Products by Revenue")

    top_products = get_top_products()

    fig = px.bar(
        top_products,
        x="revenue",
        y="product_name",
        orientation="h",
        color="revenue",
        title="Top Products"
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ==========================
    # Revenue by Category
    # ==========================

    st.subheader("📊 Revenue by Category")

    category = get_category_sales()

    fig2 = px.pie(
        category,
        names="category",
        values="revenue",
        hole=0.45,
        title="Category Revenue Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.divider()

    # ==========================
    # Product Performance Table
    # ==========================

    st.subheader("📋 Product Performance")

    st.dataframe(
        top_products,
        use_container_width=True
    )
    
    