-- AVG + GROUP BY - average salary per department.
SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department;
