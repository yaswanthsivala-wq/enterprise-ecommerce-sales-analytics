import streamlit as st
import plotly.express as px

from utils.queries import (
    get_kpi_data,
    get_monthly_sales,
    get_order_status,
    get_sales_by_country,
    get_sales_data
)


def show_sales():

    st.title("📈 Sales Analytics Dashboard")


    # ==========================
    # KPI Cards
    # ==========================

    kpi = get_kpi_data().iloc[0]


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "🛒 Total Orders",
        f"{int(kpi['total_orders']):,}"
    )


    col2.metric(
        "💰 Revenue",
        f"${kpi['total_revenue']:,.2f}"
    )


    col3.metric(
        "👥 Customers",
        f"{int(kpi['total_customers']):,}"
    )


    col4.metric(
        "⭐ Avg Order Value",
        f"${kpi['avg_order_value']:,.2f}"
    )


    st.divider()


    # ==========================
    # Monthly Revenue Trend
    # ==========================

    st.subheader(
        "📈 Monthly Revenue Trend"
    )


    monthly_sales = get_monthly_sales()


    fig = px.line(
        monthly_sales,
        x="month",
        y="revenue",
        markers=True,
        title="Revenue Growth Over Time"
    )


    st.plotly_chart(
        fig,
        width="stretch"
    )


    st.divider()


    # ==========================
    # Revenue By Country
    # ==========================

    st.subheader(
        "🌎 Revenue by Country"
    )


    country_sales = get_sales_by_country()


    fig2 = px.bar(
        country_sales,
        x="country",
        y="revenue",
        title="Revenue Contribution by Country"
    )


    st.plotly_chart(
        fig2,
        width="stretch"
    )


    st.divider()


    # ==========================
    # Order Status
    # ==========================

    st.subheader(
        "📦 Order Status Analysis"
    )


    status = get_order_status()


    fig3 = px.pie(
        status,
        names="status",
        values="orders",
        hole=0.45,
        title="Order Status Distribution"
    )


    st.plotly_chart(
        fig3,
        width="stretch"
    )


    st.divider()


    # ==========================
    # Sales Table
    # ==========================

    st.subheader(
        "📋 Sales Transactions"
    )


    sales = get_sales_data()


    st.dataframe(
        sales,
        width="stretch"
    )