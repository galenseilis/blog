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

-- Query 4: Nested query with depth 1 (new set of tables)
SELECT a.first_name, a.last_name, b.order_id
FROM (SELECT first_name, last_name, employee_id FROM foo) a
JOIN (SELECT order_id, customer_id FROM bar) b ON a.employee_id = b.customer_id;

-- Query 5: Nested query with depth 2 (new set of tables)
SELECT a.first_name, a.last_name, b.order_id
FROM (SELECT first_name, last_name, employee_id FROM (SELECT first_name, last_name, employee_id FROM foo) a) a
JOIN (SELECT order_id, customer_id FROM (SELECT order_id, customer_id FROM bar) b) b ON a.employee_id = b.customer_id;

-- Query 6: Common Table Expression (CTE) with subsequent query (new set of tables)
WITH product_prices AS (
    SELECT b.product_name, b.product_id
    FROM baz b
)
SELECT b.order_id, b.product_name, p.price
FROM bar b
JOIN baz p ON b.order_id = p.product_id;

-- Query 7: Include 'foo' in the query (placeholder)
SELECT a.first_name, a.last_name
FROM (SELECT first_name, last_name FROM foo) a;
