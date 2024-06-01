-- CTE to calculate the total work hours for each employee
WITH total_work_hours AS (
    SELECT 
        employee_id, 
        -- Calculate total work hours by summing the difference between out_time and in_time, rounded up to the nearest minute
        SUM(TIME_TO_SEC(TIMEDIFF(out_time, in_time)) / 3600 + IF(TIME_TO_SEC(TIMEDIFF(out_time, in_time)) % 60 = 0, 0, 1) / 60) AS total_hours
    FROM 
        logs
    GROUP BY 
        employee_id
)

-- Main query to find employees who have not met their needed hours
SELECT 
    e.employee_id
FROM 
    employees AS e
LEFT JOIN 
    total_work_hours USING (employee_id)
WHERE 
    e.needed_hours > IFNULL(total_hours, 0);
