-- LEFT JOIN - all departments, even with no employees.
SELECT d.name, e.name FROM departments d LEFT JOIN employees e ON e.department = d.name;
