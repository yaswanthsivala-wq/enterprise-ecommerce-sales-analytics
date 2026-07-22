import streamlit as st


st.set_page_config(
    page_title="Enterprise Ecommerce Analytics",
    page_icon="📊",
    layout="wide"
)


st.title(
    "📊 Enterprise Ecommerce Analytics Platform"
)


st.markdown(
"""
## Welcome Dashboard

Navigate using the left sidebar.

---

## Available Dashboards

📈 Sales Dashboard

Analyze:
- Revenue trends
- Order status
- Country sales
- Monthly performance


👥 Customer Dashboard

Analyze:
- Customer distribution
- Country-wise customers
- Customer behavior


📦 Product Dashboard

Analyze:
- Product performance
- Category sales
- Top selling products


---

## Technology Stack

🐍 Python

🐘 PostgreSQL

🔗 SQLAlchemy

☁️ Supabase

📊 Streamlit

📈 Plotly


---

## Data Pipeline


CSV Data

⬇️

ETL Pipeline

⬇️

Supabase PostgreSQL

⬇️

Analytics Layer

⬇️

Interactive Dashboard


"""
)