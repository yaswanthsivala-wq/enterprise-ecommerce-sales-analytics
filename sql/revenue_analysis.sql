-- ==========================================
-- Revenue Analytics
-- Business KPIs and Sales Performance
-- ==========================================


-- Total Revenue

SELECT
    SUM(total_amount) AS total_revenue
FROM orders;



-- Total Number of Orders

SELECT
    COUNT(order_id) AS total_orders
FROM orders;



-- Average Order Value

SELECT
    AVG(total_amount) AS average_order_value
FROM orders;



-- Monthly Revenue Trend

SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;



-- Revenue by Order Status

SELECT
    status,
    SUM(total_amount) AS revenue,
    COUNT(order_id) AS orders
FROM orders
GROUP BY status
ORDER BY revenue DESC;