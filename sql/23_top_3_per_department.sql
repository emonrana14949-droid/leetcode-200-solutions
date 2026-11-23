-- Top 3 per Department - window function + filter.
SELECT name, department, salary FROM (SELECT name, department, salary, ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn FROM employees) WHERE rn <= 3;
