-- Join Three Tables - order with customer name and product.
SELECT o.id, c.name AS customer, o.product, o.amount FROM orders o JOIN customers c ON o.customer_id = c.id;
