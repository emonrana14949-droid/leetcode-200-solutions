-- COALESCE - show 'No Manager' when manager is NULL.
SELECT name, COALESCE((SELECT name FROM employees m WHERE m.id = e.manager_id), 'No Manager') AS manager FROM employees e;
