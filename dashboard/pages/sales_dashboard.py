import streamlit as st
import plotly.express as px
from datetime import date, timedelta

from utils.queries import (
    get_filtered_sales_kpis,
    get_daily_sales_filtered,
    get_sales_by_country,
    get_order_status,
    get_top_products,
    get_monthly_growth,
    get_recent_orders
)


def show_sales():

    st.title("📈 Sales Analytics Dashboard")

    st.markdown(
        "### Enterprise E-Commerce Sales Performance"
    )


    # ======================================
    # SIDEBAR FILTERS
    # ======================================

    st.sidebar.header(
        "🔎 Sales Filters"
    )


    start_date = st.sidebar.date_input(
        "📅 Start Date",
        date.today() - timedelta(days=365)
    )


    end_date = st.sidebar.date_input(
        "📅 End Date",
        date.today()
    )


    status_filter = st.sidebar.selectbox(
        "📦 Order Status",
        [
            "All",
            "Completed",
            "Pending",
            "Cancelled"
        ]
    )


    country_data = get_sales_by_country()


    country_filter = st.sidebar.selectbox(
        "🌎 Country",
        ["All"] + country_data["country"].tolist()
    )


    # ======================================
    # KPI CARDS
    # ======================================

    kpi = get_filtered_sales_kpis(
    country_filter,
    status_filter
).iloc[0]



    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.metric(
            "🛒 Total Orders",
            f"{int(kpi['total_orders']):,}"
        )


    with col2:
        st.metric(
            "💰 Revenue",
            f"${kpi['total_revenue']:,.2f}"
        )


    with col3:
        st.metric(
            "👥 Customers",
            f"{int(kpi['total_customers']):,}"
        )


    with col4:
        st.metric(
            "⭐ Avg Order Value",
            f"${kpi['avg_order_value']:,.2f}"
        )


    st.divider()


    # ======================================
    # MONTHLY GROWTH
    # ======================================

    st.subheader(
        "📊 Monthly Growth"
    )


    growth = get_monthly_growth()


    if len(growth) > 1:

        latest_growth = growth.iloc[-1]["growth_percentage"]

        st.metric(
            "Revenue Growth %",
            f"{latest_growth:.2f}%"
        )


    st.divider()


    # ======================================
    # DAILY SALES TREND
    # ======================================

    st.subheader(
        "📈 Daily Revenue Trend"
    )


    daily_sales = get_daily_sales_filtered(
        start_date,
        end_date
    )


    fig = px.line(
        daily_sales,
        x="sales_date",
        y="revenue",
        markers=True,
        title="Daily Revenue"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.divider()


    # ======================================
    # COUNTRY REVENUE
    # ======================================

    st.subheader(
        "🌎 Revenue By Country"
    )


    country_sales = get_sales_by_country()


    if country_filter != "All":

        country_sales = country_sales[
            country_sales["country"] == country_filter
        ]


    fig2 = px.bar(
        country_sales,
        x="country",
        y="revenue",
        title="Revenue Contribution"
    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )


    st.divider()


    # ======================================
    # ORDER STATUS
    # ======================================

    st.subheader(
        "📦 Order Status Analysis"
    )


    status = get_order_status(
        country_filter
    )


    if status_filter != "All":

        status = status[
            status["status"] == status_filter
        ]


    fig3 = px.pie(
        status,
        names="status",
        values="orders",
        hole=0.45,
        title="Order Status Distribution"
    )


    st.plotly_chart(
        fig3,
        use_container_width=True
    )


    st.divider()


    # ======================================
    # TOP PRODUCTS
    # ======================================

    st.subheader(
        "🏆 Top Selling Products"
    )


    products = get_top_products()


    st.dataframe(
        products,
        use_container_width=True
    )


    st.divider()


    # ======================================
    # RECENT TRANSACTIONS
    # ======================================

    st.subheader(
        "🧾 Latest Customer Transactions"
    )


    recent = get_recent_orders()


    st.dataframe(
        recent,
        use_container_width=True
    )