-- Window ROW_NUMBER - number employees inside each department by salary.
SELECT name, department, salary, ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn FROM employees;
