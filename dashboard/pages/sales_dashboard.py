import streamlit as st
import pandas as pd
import plotly.express as px

from database import engine


def show_sales():

    st.title("📈 Sales Dashboard")

    query = """
    SELECT
        o.order_date,
        o.status,
        o.total_amount,
        c.country,
        p.category
    FROM orders o
    JOIN customers c
        ON o.customer_id=c.customer_id
    JOIN order_items oi
        ON o.order_id=oi.order_id
    JOIN products p
        ON oi.product_id=p.product_id
    """

    df = pd.read_sql(query, engine)

    # --------------------------
    # Sidebar Filters
    # --------------------------

    st.sidebar.header("Filters")

    country = st.sidebar.multiselect(
        "Country",
        sorted(df["country"].unique()),
        default=sorted(df["country"].unique())
    )

    status = st.sidebar.multiselect(
        "Order Status",
        sorted(df["status"].unique()),
        default=sorted(df["status"].unique())
    )

    category = st.sidebar.multiselect(
        "Category",
        sorted(df["category"].unique()),
        default=sorted(df["category"].unique())
    )

    df = df[
        (df.country.isin(country))
        &
        (df.status.isin(status))
        &
        (df.category.isin(category))
    ]

    # --------------------------
    # KPI Cards
    # --------------------------

    revenue = df["total_amount"].sum()
    orders = len(df)
    avg = df["total_amount"].mean()

    col1, col2, col3 = st.columns(3)

    col1.metric("Revenue", f"${revenue:,.0f}")

    col2.metric("Orders", orders)

    col3.metric("Average Order Value", f"${avg:,.2f}")

    st.divider()

    # --------------------------
    # Monthly Revenue
    # --------------------------

    df["month"] = pd.to_datetime(
        df["order_date"]
    ).dt.to_period("M").astype(str)

    monthly = (
        df.groupby("month")["total_amount"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly,
        x="month",
        y="total_amount",
        markers=True,
        title="Monthly Revenue"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------
    # Two Charts
    # --------------------------

    left, right = st.columns(2)

    status_df = (
        df.groupby("status")["total_amount"]
        .sum()
        .reset_index()
    )

    fig2 = px.pie(
        status_df,
        names="status",
        values="total_amount",
        hole=.5,
        title="Revenue by Status"
    )

    left.plotly_chart(
        fig2,
        use_container_width=True
    )

    country_df = (
        df.groupby("country")["total_amount"]
        .sum()
        .reset_index()
    )

    fig3 = px.bar(
        country_df,
        x="country",
        y="total_amount",
        title="Revenue by Country"
    )

    right.plotly_chart(
        fig3,
        use_container_width=True
    )

    # --------------------------
    # Category Revenue
    # --------------------------

    category_df = (
        df.groupby("category")["total_amount"]
        .sum()
        .reset_index()
    )

    fig4 = px.bar(
        category_df,
        x="category",
        y="total_amount",
        color="category",
        title="Revenue by Category"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    st.subheader("Sales Dataset")

    st.dataframe(
        df,
        use_container_width=True
    )