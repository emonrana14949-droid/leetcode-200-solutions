-- Window Running Total - cumulative order amount by date.
SELECT order_date, amount, SUM(amount) OVER (ORDER BY order_date) AS running_total FROM orders;
