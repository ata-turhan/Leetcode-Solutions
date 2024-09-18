-- Selecting the second highest distinct salary from the Employee table
SELECT 
    IF(COUNT(e.salary) >= 2, MIN(e.salary), NULL) AS SecondHighestSalary
FROM 
    (SELECT DISTINCT salary 
     FROM employee 
     ORDER BY salary DESC 
     LIMIT 2) AS e;
