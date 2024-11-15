WITH EmployeeRanked AS (
    -- Rank each employee's salary records by month within each employee, in descending order
    SELECT 
        id, 
        month, 
        salary, 
        RANK() OVER (PARTITION BY id ORDER BY month DESC) AS month_rank
    FROM employee
),
EmployeeMonthlySalaries AS (
    -- Filter out each employee's most recent month to only consider previous months
    SELECT 
        id, 
        month, 
        salary 
    FROM EmployeeRanked 
    WHERE month_rank != 1
)
-- Calculate cumulative salary by summing each month’s salary with the previous two months, if available
SELECT 
    curr_month.id, 
    curr_month.month, 
    (curr_month.salary + IFNULL(prev_month.salary, 0) + IFNULL(prev_two_months.salary, 0)) AS salary
FROM 
    EmployeeMonthlySalaries AS curr_month
LEFT JOIN 
    EmployeeMonthlySalaries AS prev_month ON curr_month.id = prev_month.id AND curr_month.month = prev_month.month + 1
LEFT JOIN 
    EmployeeMonthlySalaries AS prev_two_months ON curr_month.id = prev_two_months.id AND curr_month.month = prev_two_months.month + 2
ORDER BY 
    curr_month.id ASC, 
    curr_month.month DESC;
