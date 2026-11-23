-- CASE - label each salary as High, Medium or Low.
SELECT name, salary, CASE WHEN salary >= 60000 THEN 'High' WHEN salary >= 40000 THEN 'Medium' ELSE 'Low' END AS band FROM employees;
