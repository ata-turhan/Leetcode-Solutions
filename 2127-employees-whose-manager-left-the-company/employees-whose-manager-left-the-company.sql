SELECT employee_id 
FROM employees 
WHERE salary < 30000 
AND manager_id IS NOT NULL 
AND manager_id NOT IN (SELECT employee_id FROM employees) 
ORDER BY employee_id;

