import pandas as pd

from database import engine


# =====================================================
# EXECUTIVE DASHBOARD KPI
# =====================================================

def get_kpi_data():
    
    query = """

    SELECT

        (
            SELECT SUM(total_amount)
            FROM orders
        ) AS total_revenue,


        (
            SELECT COUNT(*)
            FROM orders
        ) AS total_orders,


        (
            SELECT COUNT(*)
            FROM customers
        ) AS total_customers,


        (
            SELECT AVG(total_amount)
            FROM orders
        ) AS avg_order_value

    """

    return pd.read_sql(
        query,
        engine
    ).iloc[0]


# =====================================================
# SALES DASHBOARD KPI FILTER
# =====================================================

def get_date_filtered_kpi(
        start_date,
        end_date
):

    query = f"""

    SELECT

        COUNT(order_id) AS total_orders,

        SUM(total_amount) AS total_revenue,

        COUNT(DISTINCT customer_id)
            AS total_customers,

        AVG(total_amount)
            AS avg_order_value


    FROM orders


    WHERE order_date BETWEEN '{start_date}'
    AND '{end_date}';

    """

    return pd.read_sql(query, engine)



# =====================================================
# DAILY SALES
# =====================================================

def get_daily_sales_filtered(
        start_date,
        end_date
):

    query = f"""

    SELECT

        DATE(order_date) AS sales_date,

        SUM(total_amount) AS revenue,

        COUNT(order_id) AS orders


    FROM orders


    WHERE order_date BETWEEN '{start_date}'
    AND '{end_date}'


    GROUP BY DATE(order_date)


    ORDER BY sales_date;

    """

    return pd.read_sql(query, engine)



# =====================================================
# MONTHLY SALES
# =====================================================

def get_monthly_sales():

    query = """

    SELECT

        DATE_TRUNC(
            'month',
            order_date
        ) AS month,


        SUM(total_amount)
        AS revenue


    FROM orders


    GROUP BY month


    ORDER BY month;

    """

    return pd.read_sql(query, engine)



# =====================================================
# MONTHLY GROWTH
# =====================================================

def get_monthly_growth():

    query = """

    WITH monthly AS (

        SELECT

        DATE_TRUNC(
            'month',
            order_date
        ) AS month,


        SUM(total_amount)
        AS revenue


        FROM orders


        GROUP BY month

    )


    SELECT

        month,

        revenue,


        LAG(revenue)
        OVER(
            ORDER BY month
        )
        AS previous_month,


        (
            (
            revenue -
            LAG(revenue)
            OVER(
                ORDER BY month
            )
            )
            /
            NULLIF(
            LAG(revenue)
            OVER(
                ORDER BY month
            ),
            0)
        ) * 100

        AS growth_percentage


    FROM monthly


    ORDER BY month;

    """

    return pd.read_sql(query, engine)



# =====================================================
# SALES BY COUNTRY
# =====================================================

def get_sales_by_country():

    query = """

    SELECT

        c.country,

        SUM(o.total_amount)
        AS revenue


    FROM customers c


    JOIN orders o

        ON c.customer_id=o.customer_id


    GROUP BY c.country


    ORDER BY revenue DESC;

    """

    return pd.read_sql(query, engine)



# =====================================================
# ORDER STATUS
# =====================================================

def get_order_status(
        country="All"
):

    query = """

    SELECT

        o.status,

        COUNT(o.order_id)
        AS orders


    FROM orders o


    JOIN customers c

        ON o.customer_id=c.customer_id


    WHERE 1=1

    """

    if country != "All":

        query += f"""

        AND c.country='{country}'

        """

    query += """

    GROUP BY o.status;


    """

    return pd.read_sql(query, engine)



# =====================================================
# TOP PRODUCTS
# =====================================================

def get_top_products(
        limit=10
):

    query = f"""

    SELECT

        p.product_name,

        p.category,

        SUM(oi.quantity)
        AS units_sold,


        SUM(
            oi.quantity * oi.price
        )
        AS revenue


    FROM products p


    JOIN order_items oi

        ON p.product_id =
        oi.product_id


    GROUP BY

        p.product_name,

        p.category


    ORDER BY revenue DESC


    LIMIT {limit};

    """

    return pd.read_sql(query, engine)



# =====================================================
# CATEGORY SALES
# =====================================================

def get_category_sales():

    query = """

    SELECT

        p.category,

        SUM(oi.quantity)
        AS units_sold,


        SUM(
            oi.quantity * oi.price
        )
        AS revenue


    FROM products p


    JOIN order_items oi

        ON p.product_id =
        oi.product_id


    GROUP BY p.category


    ORDER BY revenue DESC;

    """

    return pd.read_sql(query, engine)



# =====================================================
# RECENT ORDERS
# =====================================================

def get_recent_orders(
        limit=10
):

    query = f"""

    SELECT

        o.order_id,

        o.order_date,

        c.first_name,

        c.last_name,

        c.country,

        o.status,

        o.total_amount


    FROM orders o


    JOIN customers c

        ON o.customer_id=c.customer_id


    ORDER BY o.order_date DESC


    LIMIT {limit};

    """

    return pd.read_sql(query, engine)



# =====================================================
# PRODUCT KPI
# =====================================================

def get_product_kpis():

    query = """

    SELECT

        COUNT(DISTINCT product_id)
        AS total_products,


        SUM(quantity)
        AS units_sold,


        SUM(quantity * price)
        AS total_revenue


    FROM order_items;

    """

    return pd.read_sql(query, engine)



# =====================================================
# CUSTOMER KPI
# =====================================================

def get_customer_kpis():

    query = """

    SELECT


        COUNT(DISTINCT c.customer_id)
        AS total_customers,


        SUM(o.total_amount)
        AS total_revenue,


        AVG(o.total_amount)
        AS avg_customer_value


    FROM customers c


    JOIN orders o

    ON c.customer_id=o.customer_id;

    """

    return pd.read_sql(query, engine)



# =====================================================
# TOP CUSTOMERS
# =====================================================

def get_top_customers(
        limit=10
):

    query=f"""

    SELECT

        c.first_name,

        c.last_name,

        c.country,


        SUM(o.total_amount)
        AS total_spent


    FROM customers c


    JOIN orders o

    ON c.customer_id=o.customer_id


    GROUP BY

        c.first_name,

        c.last_name,

        c.country


    ORDER BY total_spent DESC


    LIMIT {limit};

    """

    return pd.read_sql(query, engine)



# =====================================================
# CUSTOMER SEGMENTS
# =====================================================

def get_customer_segments():

    query = """

    SELECT

        c.first_name,

        c.last_name,

        c.country,


        SUM(o.total_amount)
        AS total_spent,


        CASE

        WHEN SUM(o.total_amount)>=5000

            THEN 'VIP Customer'


        WHEN SUM(o.total_amount)>=2000

            THEN 'High Value Customer'


        WHEN SUM(o.total_amount)>=500

            THEN 'Regular Customer'


        ELSE

            'Low Value Customer'


        END AS customer_segment


    FROM customers c


    JOIN orders o

    ON c.customer_id=o.customer_id


    GROUP BY

        c.first_name,

        c.last_name,

        c.country;


    """

    return pd.read_sql(query, engine)



# =====================================================
# CUSTOMER DASHBOARD FILTER
# =====================================================

def get_customer_dashboard_data(
        country="All"
):

    query = """

    SELECT

        c.customer_id,

        c.first_name,

        c.last_name,

        c.country,


        SUM(o.total_amount)
        AS total_spent


    FROM customers c


    JOIN orders o

    ON c.customer_id=o.customer_id


    WHERE 1=1

    """

    if country!="All":

        query += f"""

        AND c.country='{country}'

        """


    query += """

    GROUP BY

        c.customer_id,

        c.first_name,

        c.last_name,

        c.country


    ORDER BY total_spent DESC;

    """


    return pd.read_sql(query, engine)
# =====================================================
# FILTERED SALES KPI
# Country + Status Filters
# =====================================================

def get_filtered_sales_kpis(
        country="All",
        status="All"
):

    query = """

    SELECT

        COUNT(DISTINCT o.order_id)
            AS total_orders,

        SUM(o.total_amount)
            AS total_revenue,

        COUNT(DISTINCT o.customer_id)
            AS total_customers,

        AVG(o.total_amount)
            AS avg_order_value


    FROM orders o


    JOIN customers c

        ON o.customer_id = c.customer_id


    WHERE 1=1

    """


    if country != "All":

        query += f"""

        AND c.country = '{country}'

        """


    if status != "All":

        query += f"""

        AND o.status = '{status}'

        """


    return pd.read_sql(
        query,
        engine
    )
# =====================================================
# CUSTOMER COUNTRIES
# =====================================================

def get_customer_countries():

    query = """
    SELECT DISTINCT
        country

    FROM customers

    ORDER BY country;
    """

    return pd.read_sql(
        query,
        engine
    )

# =====================================================
# CUSTOMER SEGMENT LIST
# =====================================================

def get_customer_segment_list():

    query = """

    SELECT DISTINCT

        CASE

            WHEN customer_total.total_spent >= 5000
                THEN 'VIP Customer'

            WHEN customer_total.total_spent >= 2000
                THEN 'High Value Customer'

            WHEN customer_total.total_spent >= 500
                THEN 'Regular Customer'

            ELSE 'Low Value Customer'

        END AS customer_segment


    FROM

    (

        SELECT

            customer_id,

            SUM(total_amount) AS total_spent


        FROM orders


        GROUP BY customer_id

    ) customer_total


    ORDER BY customer_segment;

    """


    return pd.read_sql(
        query,
        engine
    )
# ==========================================
# CUSTOMER DASHBOARD DATA
# ==========================================

def get_customer_dashboard_data(
        country="All",
        segment="All"
):

    query = """
    SELECT

        c.customer_id,

        c.first_name,

        c.last_name,

        c.country,

        SUM(o.total_amount) AS total_spent,


        CASE

            WHEN SUM(o.total_amount) >= 5000
                THEN 'VIP Customer'

            WHEN SUM(o.total_amount) >= 2000
                THEN 'High Value Customer'

            WHEN SUM(o.total_amount) >= 500
                THEN 'Regular Customer'

            ELSE 'Low Value Customer'

        END AS customer_segment


    FROM customers c


    JOIN orders o

        ON c.customer_id = o.customer_id


    WHERE 1=1

    """


    if country != "All":

        query += f"""

        AND c.country = '{country}'

        """



    query += """

    GROUP BY

        c.customer_id,

        c.first_name,

        c.last_name,

        c.country

    """



    if segment != "All":

        query += f"""

        HAVING

        CASE

            WHEN SUM(o.total_amount) >= 5000
                THEN 'VIP Customer'

            WHEN SUM(o.total_amount) >= 2000
                THEN 'High Value Customer'

            WHEN SUM(o.total_amount) >= 500
                THEN 'Regular Customer'

            ELSE 'Low Value Customer'

        END = '{segment}'

        """



    query += """

    ORDER BY total_spent DESC;

    """


    return pd.read_sql(
        query,
        engine
    )



# ==========================================
# CUSTOMER COUNTRIES
# ==========================================

def get_customer_countries():

    query = """

    SELECT DISTINCT country

    FROM customers

    ORDER BY country;

    """

    return pd.read_sql(
        query,
        engine
    )



# ==========================================
# CUSTOMER SEGMENTS
# ==========================================

def get_customer_segment_list():

    query = """

    SELECT DISTINCT

    CASE

        WHEN total_spent >= 5000
            THEN 'VIP Customer'

        WHEN total_spent >= 2000
            THEN 'High Value Customer'

        WHEN total_spent >= 500
            THEN 'Regular Customer'

        ELSE 'Low Value Customer'


    END AS customer_segment


    FROM

    (

        SELECT

        customer_id,

        SUM(total_amount) AS total_spent


        FROM orders


        GROUP BY customer_id

    ) x


    ORDER BY customer_segment;

    """


    return pd.read_sql(
        query,
        engine
    )