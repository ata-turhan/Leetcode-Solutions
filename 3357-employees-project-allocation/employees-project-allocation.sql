-- CTE to calculate the average workload per team for each project
WITH TeamAvgWorkloads AS (
    SELECT 
        e.employee_id,
        p.project_id,
        e.name AS employee_name,
        p.workload,
        AVG(p.workload) OVER (PARTITION BY e.team) AS team_avg_workload
    FROM 
        employees AS e
    JOIN 
        project AS p USING (employee_id)
)

-- Main query to select employees with workloads greater than the team's average workload
SELECT 
    employee_id, 
    project_id, 
    employee_name, 
    workload AS project_workload
FROM 
    TeamAvgWorkloads 
WHERE 
    workload > team_avg_workload 
ORDER BY 
    employee_id, project_id;
