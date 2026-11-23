-- Window NTILE - put salaries into 4 quartiles.
SELECT name, salary, NTILE(4) OVER (ORDER BY salary) AS quartile FROM employees;
