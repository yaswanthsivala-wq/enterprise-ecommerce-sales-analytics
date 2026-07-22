-- ==========================================
-- Product Analytics
-- Product and Category Performance
-- ==========================================


-- Revenue by Category

SELECT
    p.category,
    SUM(oi.quantity * oi.price) AS revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;



-- Top Selling Products

SELECT
    p.product_name,
    SUM(oi.quantity) AS units_sold,
    SUM(oi.quantity * oi.price) AS revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;



-- Inventory Overview

SELECT
    product_name,
    inventory
FROM products
ORDER BY inventory ASC;
