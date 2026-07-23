-- Total Revenue

SELECT 
    SUM(total_amount) AS total_revenue
FROM orders;


-- Total Orders

SELECT
    COUNT(order_id) AS total_orders
FROM orders;


-- Total Customers

SELECT
    COUNT(customer_id) AS total_customers
FROM customers;


-- Average Order Value

SELECT
    AVG(total_amount) AS avg_order_value
FROM orders;


-- Monthly Revenue Trend

SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;


-- Revenue By Country

SELECT
    c.country,
    SUM(o.total_amount) AS revenue
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
GROUP BY c.country
ORDER BY revenue DESC;


-- Revenue By Category

SELECT
    p.category,
    SUM(oi.quantity * oi.price) AS revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;