import streamlit as st
import pandas as pd
import plotly.express as px

from database import engine


def show_executive():

    st.title("📊 Executive Dashboard")

    st.markdown(
        "### Enterprise E-Commerce Sales Analytics Platform"
    )


    # ==========================
    # FILTERS
    # ==========================

    st.sidebar.header(
        "🔎 Dashboard Filters"
    )


    countries = pd.read_sql(
        """
        SELECT DISTINCT country
        FROM customers
        ORDER BY country;
        """,
        engine
    )


    categories = pd.read_sql(
        """
        SELECT DISTINCT category
        FROM products
        ORDER BY category;
        """,
        engine
    )


    selected_country = st.sidebar.selectbox(
        "🌎 Country",
        ["All"] + countries["country"].tolist()
    )


    selected_category = st.sidebar.selectbox(
        "📦 Category",
        ["All"] + categories["category"].tolist()
    )


    # ==========================
    # MAIN QUERY
    # ==========================


    query = """

    SELECT

        o.order_id,
        o.order_date,
        o.status,
        o.total_amount,


        c.customer_id,
        c.country,


        oi.quantity,
        oi.price,


        p.category,
        p.product_name


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
            "No data available"
        )

        return



    # ==========================
    # REMOVE DUPLICATE ORDERS
    # ==========================


    orders = (

        df[
            [
                "order_id",
                "order_date",
                "total_amount",
                "customer_id",
                "country",
                "status"
            ]

        ]

        .drop_duplicates()

    )



    # ==========================
    # KPI
    # ==========================


    total_revenue = (
        orders["total_amount"]
        .sum()
    )


    total_orders = (
        orders["order_id"]
        .nunique()
    )


    total_customers = (
        orders["customer_id"]
        .nunique()
    )


    avg_order_value = (

        total_revenue /
        total_orders

    )



    col1,col2,col3,col4 = st.columns(4)


    col1.metric(
        "💰 Total Revenue",
        f"${total_revenue:,.2f}"
    )


    col2.metric(
        "📦 Total Orders",
        f"{total_orders:,}"
    )


    col3.metric(
        "👥 Customers",
        f"{total_customers:,}"
    )


    col4.metric(
        "🛒 Avg Order Value",
        f"${avg_order_value:,.2f}"
    )



    st.divider()



    # ==========================
    # MONTHLY REVENUE
    # ==========================


    st.subheader(
        "📈 Monthly Revenue Trend"
    )


    monthly = orders.copy()


    monthly["month"] = pd.to_datetime(
        monthly["order_date"]
    ).dt.to_period("M").astype(str)



    monthly_sales = (

        monthly

        .groupby("month")

        ["total_amount"]

        .sum()

        .reset_index()

    )



    fig = px.line(

        monthly_sales,

        x="month",

        y="total_amount",

        markers=True,

        title="Monthly Revenue"

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



    st.divider()



    # ==========================
    # COUNTRY REVENUE
    # ==========================


    col1,col2 = st.columns(2)



    with col1:


        st.subheader(
            "🌎 Revenue by Country"
        )


        country_sales = (

            orders

            .groupby("country")

            ["total_amount"]

            .sum()

            .reset_index()

        )


        fig = px.bar(

            country_sales,

            x="country",

            y="total_amount"

        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )



    # ==========================
    # CATEGORY REVENUE
    # ==========================


    with col2:


        st.subheader(
            "📦 Revenue by Category"
        )


        category_sales = (

            df

            .assign(

                revenue=
                df["quantity"] *
                df["price"]

            )

            .groupby("category")

            ["revenue"]

            .sum()

            .reset_index()

        )


        fig = px.pie(

            category_sales,

            names="category",

            values="revenue",

            hole=0.45

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )



    st.divider()



    # ==========================
    # STATUS
    # ==========================


    st.subheader(
        "📦 Order Status Overview"
    )


    status = (

        orders

        .groupby("status")

        ["order_id"]

        .count()

        .reset_index()

    )


    fig = px.pie(

        status,

        names="status",

        values="order_id",

        hole=0.45

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.divider()



    # ==========================
    # TOP PRODUCTS
    # ==========================


    st.subheader(
        "🏆 Top Performing Products"
    )


    top_products = (

        df

        .assign(

            revenue=
            df["quantity"] *
            df["price"]

        )

        .groupby(
            [
                "product_name",
                "category"
            ]
        )

        ["revenue"]

        .sum()

        .reset_index()

        .sort_values(
            "revenue",
            ascending=False
        )

        .head(10)

    )


    st.dataframe(

        top_products,

        use_container_width=True

    )