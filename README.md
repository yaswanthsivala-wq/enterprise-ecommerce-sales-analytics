# 📊 Enterprise Ecommerce Sales Analytics Platform

An end-to-end **Enterprise E-Commerce Sales Analytics Platform** built using **Python, PostgreSQL, SQL, Streamlit, and Plotly**.

This project simulates a real-world Business Intelligence (BI) solution by generating ecommerce transaction data, building an ETL pipeline, storing analytical data in a PostgreSQL database, and delivering interactive dashboards for executive decision-making.

The platform enables businesses to analyze:

- 📈 Sales performance and revenue trends
- 🌎 Geographic revenue distribution
- 📦 Product and category performance
- 👥 Customer purchasing behavior
- 🎯 Customer segmentation and value analysis

---

## 🚀 Project Highlights

- Built an automated **ETL pipeline** to extract, transform, and load ecommerce data.
- Designed a PostgreSQL data model for customers, products, orders, and transactions.
- Developed SQL-based analytics queries for business metrics.
- Created interactive Streamlit dashboards with Plotly visualizations.
- Implemented customer segmentation to identify VIP and high-value customers.
- Developed executive KPI dashboards for data-driven decision-making.

---

## 🛠️ Technology Stack

### Programming
- Python

### Database
- PostgreSQL
- Supabase

### Data Engineering
- ETL Pipeline
- Pandas
- SQLAlchemy

### Analytics & Visualization
- SQL
- Streamlit
- Plotly

### Version Control
- Git
- GitHub

---

## 📊 Dashboard Screenshots

### Executive Dashboard

![Executive Dashboard](screenshots/executive_dashboard.png)

Provides high-level business KPIs including:
- Total Revenue
- Total Orders
- Average Order Value
- Revenue Trends
- Business Performance Overview


### Sales Dashboard

![Sales Dashboard](screenshots/sales_dashboard.png)

Analyzes:
- Revenue trends over time
- Sales performance
- Geographic revenue distribution
- Order patterns


### Product Dashboard

![Product Dashboard](screenshots/product_dashboard.png)

Provides insights into:
- Product performance
- Category-level revenue analysis
- Top-performing products
- Product contribution to sales


### Customer Dashboard

![Customer Dashboard](screenshots/customer_dashboard.png)

Analyzes:
- Customer purchasing behavior
- Customer segmentation
- VIP customers
- High-value customer analysis


---

## 📁 Project Structure

```text
enterprise-ecommerce-sales-analytics/

│
├── data/
│   └── ecommerce_data.csv
│
├── screenshots/
│   ├── executive_dashboard.png
│   ├── sales_dashboard.png
│   ├── product_dashboard.png
│   └── customer_dashboard.png
│
├── app.py
├── database.py
├── etl_pipeline.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

- **app.py** → Streamlit dashboard application
- **database.py** → PostgreSQL database connection setup
- **etl_pipeline.py** → Data generation, cleaning, and loading process
- **requirements.txt** → Required Python libraries
- **screenshots/** → Dashboard images for documentation

---

## 🏗️ System Architecture

The platform follows an end-to-end analytics workflow:

```text
E-Commerce Data Generation
            |
            ↓
        ETL Pipeline
(Python + Pandas + SQLAlchemy)
            |
            ↓
    PostgreSQL Database
(Customers | Products | Orders)
            |
            ↓
    SQL Analytics Layer
(Business Metrics & KPIs)
            |
            ↓
 Streamlit + Plotly Dashboard
(Executive | Sales | Product | Customer)
```

### Data Flow Explanation

- **Data Generation:** Creates realistic ecommerce transaction data.
- **ETL Pipeline:** Cleans, transforms, and loads data into PostgreSQL.
- **Database Layer:** Stores structured customer, product, and order information.
- **SQL Analytics:** Calculates business KPIs and analytical metrics.
- **Visualization Layer:** Provides interactive dashboards using Streamlit and Plotly.