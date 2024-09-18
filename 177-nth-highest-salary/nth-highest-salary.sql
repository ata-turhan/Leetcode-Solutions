CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    -- Declare a variable M which will store the value of N-1, used for the LIMIT clause
    DECLARE M INT; 
    SET M = N - 1; 

    -- Return the Nth highest salary
    RETURN (
        SELECT DISTINCT salary
        FROM Employee
        -- Order salaries in descending order to get the highest salary first
        ORDER BY salary DESC
        -- Skip the first (N-1) highest salaries and select the next one
        LIMIT M, 1
    );
END;
