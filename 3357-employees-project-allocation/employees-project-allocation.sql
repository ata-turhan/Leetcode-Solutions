-- CTE to calculate the average workload per team
WITH avg_workloads AS (
    SELECT 
        e.employee_id,
        p.project_id,
        e.name AS employee_name,
        p.workload,
        AVG(p.workload) OVER (PARTITION BY e.team) AS avg_workload
    FROM 
        employees AS e
    JOIN 
        project AS p USING (employee_id)
)

-- Main query to select employees with workloads greater than the team average
SELECT 
    employee_id, 
    project_id, 
    employee_name, 
    workload AS project_workload
FROM 
    avg_workloads 
WHERE 
    workload > avg_workload 
ORDER BY 
    employee_id, project_id;
