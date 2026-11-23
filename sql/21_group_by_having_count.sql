-- GROUP BY + HAVING - departments with at least 2 employees.
SELECT department, COUNT(*) AS n FROM employees GROUP BY department HAVING COUNT(*) >= 2;
