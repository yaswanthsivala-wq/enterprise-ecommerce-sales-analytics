import pandas as pd

from database import engine



def get_category_sales():

    query = """
    SELECT
        p.category,
        SUM(oi.quantity) AS units_sold,
        SUM(oi.quantity * oi.price) AS revenue
    FROM products p
    JOIN order_items oi
    ON p.product_id = oi.product_id
    GROUP BY p.category
    ORDER BY revenue DESC;
    """

    return pd.read_sql(
        query,
        engine
    )



def get_customer_data(country="All"):

    if country == "All":

        query = """
        SELECT
            c.customer_id,
            c.first_name,
            c.last_name,
            c.country,
            SUM(o.total_amount) AS total_spent
        FROM customers c
        JOIN orders o
        ON c.customer_id=o.customer_id
        GROUP BY
            c.customer_id,
            c.first_name,
            c.last_name,
            c.country
        ORDER BY total_spent DESC;
        """

    else:

        query = f"""
        SELECT
            c.customer_id,
            c.first_name,
            c.last_name,
            c.country,
            SUM(o.total_amount) AS total_spent
        FROM customers c
        JOIN orders o
        ON c.customer_id=o.customer_id
        WHERE c.country='{country}'
        GROUP BY
            c.customer_id,
            c.first_name,
            c.last_name,
            c.country
        ORDER BY total_spent DESC;
        """

    return pd.read_sql(
        query,
        engine
    )



# ==============================
# Executive Dashboard Queries
# ==============================


def get_kpi_data():

    query = """
    SELECT
        COUNT(DISTINCT order_id) AS total_orders,
        SUM(total_amount) AS total_revenue,
        COUNT(DISTINCT customer_id) AS total_customers,
        AVG(total_amount) AS avg_order_value
    FROM orders;
    """

    return pd.read_sql(
        query,
        engine
    )



def get_monthly_sales():

    query = """
    SELECT
        DATE_TRUNC('month', order_date) AS month,
        SUM(total_amount) AS revenue
    FROM orders
    GROUP BY month
    ORDER BY month;
    """

    return pd.read_sql(
        query,
        engine
    )



def get_order_status():

    query = """
    SELECT
        status,
        COUNT(*) AS orders
    FROM orders
    GROUP BY status;
    """

    return pd.read_sql(
        query,
        engine
    )



def get_country_filter():

    query = """
    SELECT DISTINCT country
    FROM customers
    ORDER BY country;
    """

    return pd.read_sql(
        query,
        engine
    )
    
def get_filtered_kpi(country="All"):
    
    if country == "All":

        query = """
        SELECT
            COUNT(DISTINCT order_id) AS total_orders,
            SUM(total_amount) AS total_revenue,
            COUNT(DISTINCT customer_id) AS total_customers,
            AVG(total_amount) AS avg_order_value
        FROM orders;
        """

    else:

        query = f"""
        SELECT
            COUNT(DISTINCT o.order_id) AS total_orders,
            SUM(o.total_amount) AS total_revenue,
            COUNT(DISTINCT o.customer_id) AS total_customers,
            AVG(o.total_amount) AS avg_order_value
        FROM orders o
        JOIN customers c
        ON o.customer_id = c.customer_id
        WHERE c.country='{country}';
        """


    return pd.read_sql(
        query,
        engine
    )



def get_countries():

    query = """
    SELECT DISTINCT country
    FROM customers
    ORDER BY country;
    """

    return pd.read_sql(
        query,
        engine
    )

def get_categories():
    
    query = """
    SELECT DISTINCT category
    FROM products
    ORDER BY category;
    """

    return pd.read_sql(
        query,
        engine
    )

def get_filtered_sales(country="All", category="All"):
    
    query = """
    SELECT
        DATE_TRUNC('month', o.order_date) AS month,
        SUM(oi.quantity * oi.price) AS revenue
    FROM orders o
    JOIN order_items oi
    ON o.order_id = oi.order_id
    JOIN products p
    ON oi.product_id = p.product_id
    JOIN customers c
    ON o.customer_id = c.customer_id
    WHERE 1=1
    """

    if country != "All":
        query += f"""
        AND c.country = '{country}'
        """

    if category != "All":
        query += f"""
        AND p.category = '{category}'
        """

    query += """
    GROUP BY month
    ORDER BY month;
    """

    return pd.read_sql(
        query,
        engine
    )

def get_top_products():
    
    query = """
    SELECT
        p.product_name,
        p.category,
        SUM(oi.quantity) AS units_sold,
        SUM(oi.quantity * oi.price) AS revenue
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id
    GROUP BY
        p.product_name,
        p.category
    ORDER BY revenue DESC;
    """

    return pd.read_sql(
        query,
        engine
    )
def get_product_kpis():
    
    query = """
    SELECT
        COUNT(DISTINCT p.product_id) AS total_products,
        SUM(oi.quantity) AS units_sold,
        SUM(oi.quantity * oi.price) AS total_revenue
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id;
    """

    return pd.read_sql(
        query,
        engine
    )