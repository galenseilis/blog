-- Query 1: Simple select from one table
SELECT first_name, last_name FROM employees;

-- Query 2: Join two tables
SELECT o.order_id, c.customer_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;

-- Query 3: Join multiple tables and use aliases
SELECT o.order_id, c.customer_name, p.product_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items i ON o.order_id = i.order_id
JOIN products p ON i.product_id = p.product_id;
