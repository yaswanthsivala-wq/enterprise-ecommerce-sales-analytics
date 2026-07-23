import streamlit as st
import plotly.express as px

from utils.queries import (
    get_customer_dashboard_data,
    get_customer_countries,
    get_customer_segment_list
)


def show_customer():

    st.title("👥 Customer Analytics Dashboard")

    st.markdown(
        "### Customer Insights & Segmentation"
    )

    # ==========================================
    # SIDEBAR FILTERS
    # ==========================================

    st.sidebar.header("🔎 Customer Filters")

    countries = get_customer_countries()

    country = st.sidebar.selectbox(
        "🌎 Country",
        ["All"] + countries["country"].tolist()
    )

    segments = get_customer_segment_list()

    segment = st.sidebar.selectbox(
        "👥 Customer Segment",
        ["All"] + segments["customer_segment"].tolist()
    )

    # ==========================================
    # LOAD DATA
    # ==========================================

    customers = get_customer_dashboard_data(
        country,
        segment
    )

    if customers.empty:

        st.warning("No customers found for selected filters.")
        return

    # ==========================================
    # KPI CARDS
    # ==========================================

    total_customers = len(customers)

    total_revenue = customers["total_spent"].sum()

    avg_customer = customers["total_spent"].mean()

    vip_customers = (
        customers["customer_segment"]
        == "VIP Customer"
    ).sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "👥 Customers",
        f"{total_customers:,}"
    )

    col2.metric(
        "💰 Revenue",
        f"${total_revenue:,.2f}"
    )

    col3.metric(
        "⭐ Avg Customer Value",
        f"${avg_customer:,.2f}"
    )

    col4.metric(
        "🏆 VIP Customers",
        f"{vip_customers:,}"
    )

    st.divider()

    # ==========================================
    # TOP CUSTOMERS
    # ==========================================

    st.subheader("🏆 Top 10 Customers")

    top10 = customers.head(10).copy()

    top10["Customer"] = (
        top10["first_name"]
        + " "
        + top10["last_name"]
    )

    fig = px.bar(
        top10,
        x="total_spent",
        y="Customer",
        orientation="h",
        color="country",
        title="Highest Spending Customers"
    )

    fig.update_layout(
        yaxis={
            "categoryorder": "total ascending"
        }
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.divider()

    # ==========================================
    # CUSTOMER SEGMENTS
    # ==========================================

    st.subheader(
        "📊 Customer Segmentation"
    )

    segment_summary = (
        customers
        .groupby("customer_segment")
        .size()
        .reset_index(name="customers")
    )

    fig2 = px.pie(
        segment_summary,
        names="customer_segment",
        values="customers",
        hole=0.45,
        title="Customer Distribution"
    )

    st.plotly_chart(
        fig2,
        width="stretch"
    )

    st.divider()

    # ==========================================
    # COUNTRY DISTRIBUTION
    # ==========================================

    st.subheader(
        "🌎 Customers by Country"
    )

    country_summary = (
        customers
        .groupby("country")
        .size()
        .reset_index(name="customers")
        .sort_values(
            by="customers",
            ascending=False
        )
    )

    fig3 = px.bar(
        country_summary,
        x="country",
        y="customers",
        color="customers",
        title="Customer Distribution by Country"
    )

    st.plotly_chart(
        fig3,
        width="stretch"
    )

    st.divider()

    # ==========================================
    # CUSTOMER DETAILS
    # ==========================================

    st.subheader(
        "📋 Customer Details"
    )

    st.dataframe(
        customers,
        width="stretch"
    )