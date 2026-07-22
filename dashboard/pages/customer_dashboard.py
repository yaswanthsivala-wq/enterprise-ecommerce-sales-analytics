import streamlit as st
import plotly.express as px

from utils.queries import (
    get_customer_kpis,
    get_top_customers,
    get_customer_segments
)


def show_customer():

    st.title("👥 Customer Analytics Dashboard")


    # ==========================
    # KPI Cards
    # ==========================

    kpi = get_customer_kpis().iloc[0]


    col1, col2, col3 = st.columns(3)


    col1.metric(
        "👥 Total Customers",
        f"{int(kpi['total_customers']):,}"
    )


    col2.metric(
        "💰 Total Revenue",
        f"${kpi['total_revenue']:,.2f}"
    )


    col3.metric(
        "⭐ Avg Customer Value",
        f"${kpi['avg_customer_value']:,.2f}"
    )


    st.divider()


    # ==========================
    # Top Customers
    # ==========================

    st.subheader(
        "🏆 Top 10 Customers by Spending"
    )


    top_customers = get_top_customers()


    fig = px.bar(
        top_customers,
        x="total_spent",
        y="first_name",
        orientation="h",
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


    # ==========================
    # Customer Segmentation
    # ==========================

    st.subheader(
        "📊 Customer Segmentation"
    )


    segments = get_customer_segments()


    segment_counts = (
        segments["customer_segment"]
        .value_counts()
        .reset_index()
    )


    segment_counts.columns = [
        "segment",
        "customers"
    ]


    fig2 = px.pie(
        segment_counts,
        names="segment",
        values="customers",
        hole=0.45,
        title="Customer Segment Distribution"
    )


    st.plotly_chart(
        fig2,
        width="stretch"
    )


    st.divider()


    # ==========================
    # Customer Segment Details
    # ==========================

    st.subheader(
        "📋 Customer Segment Details"
    )


    st.dataframe(
        segments,
        width="stretch"
    )