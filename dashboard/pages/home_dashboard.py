import streamlit as st
import plotly.express as px

from utils.queries import (
    get_filtered_kpi,
    get_filtered_sales,
    get_order_status,
    get_countries,
    get_categories
)


def show_home():

    st.title("📊 Executive Ecommerce Dashboard")


    # ==========================
    # Country Filter
    # ==========================

    countries = get_countries()

    country_list = [
        "All"
    ] + countries["country"].tolist()


    selected_country = st.sidebar.selectbox(
        "🌎 Select Country",
        country_list
    )


    # ==========================
    # Category Filter
    # ==========================

    categories = get_categories()

    category_list = [
        "All"
    ] + categories["category"].tolist()


    selected_category = st.sidebar.selectbox(
        "📦 Select Category",
        category_list
    )


    # ==========================
    # KPI Cards
    # ==========================

    kpi = get_filtered_kpi(
        selected_country
    ).iloc[0]


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "🛒 Total Orders",
        f"{int(kpi['total_orders']):,}"
    )


    col2.metric(
        "💰 Total Revenue",
        f"${kpi['total_revenue']:,.2f}"
    )


    col3.metric(
        "👥 Customers",
        f"{int(kpi['total_customers']):,}"
    )


    col4.metric(
        "📦 Avg Order Value",
        f"${kpi['avg_order_value']:,.2f}"
    )


    st.divider()


    # ==========================
    # Monthly Revenue Trend
    # ==========================

    st.subheader("📈 Monthly Revenue Trend")


    sales = get_filtered_sales(
        selected_country,
        selected_category
    )


    fig = px.line(
        sales,
        x="month",
        y="revenue",
        markers=True,
        title="Revenue Growth Over Time"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ==========================
    # Order Status
    # ==========================

    st.subheader("📦 Order Status Distribution")


    status = get_order_status()


    fig2 = px.pie(
        status,
        names="status",
        values="orders",
        hole=0.4,
        title="Order Status Breakdown"
    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )