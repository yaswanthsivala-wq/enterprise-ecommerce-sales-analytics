-- ==========================================
-- Customer Analytics
-- Customer Segmentation and Behavior
-- ==========================================


-- Customer Revenue Ranking

SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.country,
    SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.country
ORDER BY total_spent DESC;



-- Top 10 Customers

SELECT
    c.first_name,
    c.last_name,
    SUM(o.total_amount) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY
    c.first_name,
    c.last_name
ORDER BY revenue DESC
LIMIT 10;

-- Customer Count by Country

SELECT
    country,
    COUNT(customer_id) AS customers
FROM customers
GROUP BY country
ORDER BY customers DESC;