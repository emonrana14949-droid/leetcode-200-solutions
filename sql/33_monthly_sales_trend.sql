-- Monthly Trend - total sales per month.
SELECT strftime('%Y-%m', order_date) AS month, SUM(amount) AS total FROM orders GROUP BY month ORDER BY month;
