-- ROUND - average salary rounded to 2 decimals.
SELECT department, ROUND(AVG(salary), 2) AS avg_salary FROM employees GROUP BY department;
