WITH RECURSIVE Hierarchy AS (
    -- Base case: Select the CEO and initialize the hierarchy
    SELECT
        employee_id AS subordinate_id,
        employee_name AS subordinate_name,
        0 AS hierarchy_level,
        salary AS subordinate_salary,
        salary AS ceo_salary
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive case: Join the CTE with the Employees table to find subordinates
    SELECT
        e.employee_id AS subordinate_id,
        e.employee_name AS subordinate_name,
        h.hierarchy_level + 1 AS hierarchy_level,
        e.salary AS subordinate_salary,
        h.ceo_salary
    FROM Employees e
    JOIN Hierarchy h ON e.manager_id = h.subordinate_id
)

-- Select and calculate the salary difference
SELECT
    subordinate_id,
    subordinate_name,
    hierarchy_level,
    subordinate_salary - ceo_salary AS salary_difference
FROM Hierarchy
WHERE hierarchy_level > 0
ORDER BY hierarchy_level ASC, subordinate_id ASC;