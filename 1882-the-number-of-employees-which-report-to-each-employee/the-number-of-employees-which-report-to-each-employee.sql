SELECT
    e1.employee_id,
    e1.name,
    COUNT(e2.employee_id) AS reports_count, -- Count of employees reporting to e1
    ROUND(AVG(e2.age)) AS average_age       -- Average age of those reporting to e1
FROM Employees e1
INNER JOIN Employees e2 
    ON e1.employee_id = e2.reports_to      -- Join employees with their subordinates
GROUP BY e1.employee_id, e1.name          -- Group by employee_id and name for accurate aggregation
ORDER BY e1.employee_id;                  -- Sort the results by employee_id
