import streamlit as st
import plotly.express as px

from utils.queries import get_customer_data


def show_customer():

    st.title("👥 Customer Dashboard")

    country = st.session_state.get(
        "country",
        "All"
    )

    customers = get_customer_data(country)

    if customers.empty:
        st.warning("No customer data available")
        return


    st.subheader(
        "Top Customers"
    )


    fig = px.bar(
        customers.head(10),
        x="first_name",
        y="total_spent",
        title="Top Customer Spending"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.subheader(
        "Customer Details"
    )


    st.dataframe(
        customers,
        use_container_width=True
    )