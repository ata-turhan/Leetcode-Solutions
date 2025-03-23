-- Select the department name, employee name, and salary for employees with the highest salary in each department
SELECT
    Department.name AS 'Department', 
    Employee.name AS 'Employee',     
    Employee.salary AS 'Salary'       
FROM
    Employee
    JOIN Department ON Employee.DepartmentId = Department.Id  -- Join Employee and Department tables on the department ID
WHERE
    -- Ensure we only select employees whose salary matches the maximum salary in their department
    Employee.Salary = (
        SELECT MAX(Salary)  -- Find the maximum salary for each department
        FROM Employee AS e  -- Aliased subquery to compare salaries
        WHERE e.DepartmentId = Employee.DepartmentId  -- Match employees within the same department
    )
ORDER BY
    Department.name,  -- Order the output by department name alphabetically
    Employee.name;    -- Order employees alphabetically within each department
