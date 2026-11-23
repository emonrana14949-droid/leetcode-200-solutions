-- Extract Year - orders per year.
SELECT strftime('%Y', order_date) AS year, COUNT(*) AS n FROM orders GROUP BY year;
