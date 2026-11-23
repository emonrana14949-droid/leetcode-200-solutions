-- INNER JOIN - employee name with department location.
SELECT e.name, d.location FROM employees e INNER JOIN departments d ON e.department = d.name;
