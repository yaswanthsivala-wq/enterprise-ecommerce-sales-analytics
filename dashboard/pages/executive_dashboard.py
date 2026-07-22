import streamlit as st
import pandas as pd
import plotly.express as px


def show_executive():

    st.title("📊 Executive Dashboard")
    st.markdown("### Enterprise E-Commerce Sales Analytics Platform")

    # ============================
    # KPI CARDS
    # ============================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="💰 Total Revenue",
            value="$1,250,000",
            delta="+12%"
        )

    with col2:
        st.metric(
            label="📦 Total Orders",
            value="5,432",
            delta="+8%"
        )

    with col3:
        st.metric(
            label="👥 Total Customers",
            value="1,284",
            delta="+5%"
        )

    with col4:
        st.metric(
            label="🛒 Average Order Value",
            value="$230.12",
            delta="+3%"
        )

    st.divider()

    # ============================
    # SAMPLE DATA
    # ============================

    revenue_df = pd.DataFrame({
        "Month": [
            "Jan", "Feb", "Mar", "Apr",
            "May", "Jun", "Jul", "Aug",
            "Sep", "Oct", "Nov", "Dec"
        ],
        "Revenue": [
            95000, 110000, 125000, 140000,
            155000, 170000, 165000, 180000,
            210000, 230000, 245000, 270000
        ]
    })

    country_df = pd.DataFrame({
        "Country": [
            "USA",
            "Canada",
            "UK",
            "Germany",
            "India"
        ],
        "Revenue": [
            500000,
            220000,
            180000,
            150000,
            200000
        ]
    })

    category_df = pd.DataFrame({
        "Category": [
            "Electronics",
            "Fashion",
            "Home",
            "Sports",
            "Beauty"
        ],
        "Revenue": [
            420000,
            260000,
            180000,
            140000,
            110000
        ]
    })

    # ============================
    # REVENUE TREND
    # ============================

    st.subheader("📈 Revenue Trend")

    fig = px.line(
        revenue_df,
        x="Month",
        y="Revenue",
        markers=True,
        title="Monthly Revenue"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ============================
    # TWO CHARTS
    # ============================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🌍 Revenue by Country")

        fig = px.bar(
            country_df,
            x="Country",
            y="Revenue"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        st.subheader("📦 Revenue by Category")

        fig = px.pie(
            category_df,
            names="Category",
            values="Revenue"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ============================
    # TOP PRODUCTS
    # ============================

    st.subheader("🏆 Top Product Categories")

    st.dataframe(
        category_df.sort_values(
            by="Revenue",
            ascending=False
        ),
        use_container_width=True
    )