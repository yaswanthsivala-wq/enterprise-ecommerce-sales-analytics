-- ==========================================
-- Geographic Analytics
-- Regional Sales Performance
-- ==========================================


-- Revenue by Country

SELECT
    c.country,
    SUM(o.total_amount) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.country
ORDER BY revenue DESC;



-- Orders by Country

SELECT
    c.country,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.country
ORDER BY total_orders DESC;