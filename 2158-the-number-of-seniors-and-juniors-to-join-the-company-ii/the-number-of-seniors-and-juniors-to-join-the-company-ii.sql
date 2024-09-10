-- Step 1: Calculate cumulative salaries of senior candidates in ascending salary order, filtering by experience
WITH OrderedSeniors AS (
    SELECT 
        employee_id, 
        salary, 
        SUM(salary) OVER (ORDER BY salary ASC) AS cum_sal 
    FROM 
        candidates 
    WHERE 
        experience = 'Senior'
),

-- Step 2: Select senior employees whose cumulative salaries do not exceed 70,000
HiredSeniors AS (
    SELECT 
        employee_id, 
        salary 
    FROM 
        OrderedSeniors 
    WHERE 
        cum_sal <= 70000
),

-- Step 3: Calculate the total salary of all hired senior employees
TotalHiredSeniorSalaries AS (
    SELECT 
        IFNULL(SUM(salary), 0) AS sum_sal 
    FROM 
        HiredSeniors
),

-- Step 4: Calculate cumulative salaries of junior candidates in ascending salary order
OrderedJuniors AS (
    SELECT 
        employee_id, 
        SUM(salary) OVER (ORDER BY salary ASC) AS cum_sal 
    FROM 
        candidates 
    WHERE 
        experience = 'Junior'
),

-- Step 5: Select junior employees whose cumulative salaries, along with hired seniors' total salaries, do not exceed 70,000
HiredJuniors AS (
    SELECT 
        employee_id 
    FROM 
        OrderedJuniors 
    WHERE 
        cum_sal + (SELECT sum_sal FROM TotalHiredSeniorSalaries) <= 70000
)

-- Step 6: Return the list of all hired employees (seniors and juniors)
SELECT 
    employee_id 
FROM 
    HiredSeniors
UNION ALL
SELECT 
    employee_id 
FROM 
    HiredJuniors;
