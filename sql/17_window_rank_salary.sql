-- Window RANK - rank employees by salary, highest first.
SELECT name, salary, RANK() OVER (ORDER BY salary DESC) AS rnk FROM employees;
