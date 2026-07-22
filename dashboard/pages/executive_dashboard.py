import streamlit as st
import pandas as pd
import plotly.express as px

from database import engine


def show_executive():

    st.title("📊 Executive Dashboard")
    st.markdown("### Enterprise E-Commerce Sales Analytics Platform")


    # ============================
    # SIDEBAR FILTERS
    # ============================

    st.sidebar.header("🔎 Dashboard Filters")


    country_query = """
    SELECT DISTINCT country
    FROM customers
    ORDER BY country;
    """

    countries_df = pd.read_sql(
        country_query,
        engine
    )

    selected_country = st.sidebar.selectbox(
        "🌎 Country",
        ["All"] + countries_df["country"].tolist()
    )


    category_query = """
    SELECT DISTINCT category
    FROM products
    ORDER BY category;
    """

    categories_df = pd.read_sql(
        category_query,
        engine
    )


    selected_category = st.sidebar.selectbox(
        "📦 Category",
        ["All"] + categories_df["category"].tolist()
    )


    # ============================
    # MAIN QUERY
    # ============================

    query = """
    SELECT
        o.order_date,
        o.total_amount,
        c.country,
        p.category,
        p.product_name,
        c.first_name,
        c.last_name

    FROM orders o

    JOIN customers c
    ON o.customer_id = c.customer_id

    JOIN order_items oi
    ON o.order_id = oi.order_id

    JOIN products p
    ON oi.product_id = p.product_id

    WHERE 1=1
    """


    if selected_country != "All":

        query += f"""
        AND c.country = '{selected_country}'
        """


    if selected_category != "All":

        query += f"""
        AND p.category = '{selected_category}'
        """


    df = pd.read_sql(
        query,
        engine
    )


    if df.empty:

        st.warning(
            "No data available for selected filters."
        )

        return


    # ============================
    # KPI CARDS
    # ============================


    total_revenue = df["total_amount"].sum()

    total_orders = df["total_amount"].count()

    total_customers = (
        df[
            ["first_name", "last_name"]
        ]
        .drop_duplicates()
        .shape[0]
    )

    avg_order_value = (
        total_revenue / total_orders
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "💰 Total Revenue",
            f"${total_revenue:,.2f}"
        )


    with col2:

        st.metric(
            "📦 Total Orders",
            f"{total_orders:,}"
        )


    with col3:

        st.metric(
            "👥 Total Customers",
            f"{total_customers:,}"
        )


    with col4:

        st.metric(
            "🛒 Average Order Value",
            f"${avg_order_value:,.2f}"
        )


    st.divider()



    # ============================
    # REVENUE TREND
    # ============================


    st.subheader(
        "📈 Monthly Revenue Trend"
    )


    df["month"] = (
        pd.to_datetime(
            df["order_date"]
        )
        .dt
        .strftime("%b")
    )


    monthly_revenue = (
        df
        .groupby("month")
        ["total_amount"]
        .sum()
        .reset_index()
    )


    fig = px.line(
        monthly_revenue,
        x="month",
        y="total_amount",
        markers=True,
        title="Revenue Over Time"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



    # ============================
    # COUNTRY + CATEGORY
    # ============================


    col1, col2 = st.columns(2)


    with col1:

        st.subheader(
            "🌎 Revenue by Country"
        )


        country_revenue = (
            df
            .groupby("country")
            ["total_amount"]
            .sum()
            .reset_index()
        )


        fig = px.bar(
            country_revenue,
            x="country",
            y="total_amount"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )



    with col2:

        st.subheader(
            "📦 Revenue by Category"
        )


        category_revenue = (
            df
            .groupby("category")
            ["total_amount"]
            .sum()
            .reset_index()
        )


        fig = px.pie(
            category_revenue,
            names="category",
            values="total_amount"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )



    st.divider()



    # ============================
    # TOP PRODUCTS
    # ============================


    st.subheader(
        "🏆 Top Performing Products"
    )


    top_products = (
        df
        .groupby("product_name")
        ["total_amount"]
        .sum()
        .reset_index()
        .sort_values(
            by="total_amount",
            ascending=False
        )
        .head(10)
    )


    st.dataframe(
        top_products,
        use_container_width=True
    )