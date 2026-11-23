-- SUM + GROUP BY - total sales per product.
SELECT product, SUM(amount) AS total_sales FROM orders GROUP BY product;
