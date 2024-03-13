WITH unique_salary_ids AS (
    SELECT 
        e1.employee_id AS id 
    FROM 
        employees AS e1 
    LEFT JOIN 
        employees AS e2 ON e1.employee_id != e2.employee_id AND e1.salary = e2.salary 
    WHERE 
        e2.salary IS NULL
)

SELECT 
    employee_id, 
    name, 
    salary, 
    DENSE_RANK() OVER (ORDER BY salary) AS team_id 
FROM 
    employees 
WHERE 
    employee_id NOT IN (SELECT id FROM unique_salary_ids) 
ORDER BY 
    team_id, 
    employee_id;
