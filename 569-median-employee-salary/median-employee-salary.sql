-- CTE to rank employees within each company based on salary (ascending), then by id
WITH RankedSalaries AS (
    SELECT 
        id,
        company,
        salary,
        RANK() OVER (PARTITION BY company ORDER BY salary ASC, id ASC) AS rank_position
    FROM 
        employee
),

-- CTE to identify companies with an odd number of employees
OddCountCompanies AS (
    SELECT 
        company, 
        COUNT(*) AS employee_count 
    FROM 
        RankedSalaries 
    GROUP BY 
        company 
    HAVING COUNT(*) % 2 = 1
),

-- CTE to identify companies with an even number of employees
EvenCountCompanies AS (
    SELECT 
        company, 
        COUNT(*) AS employee_count 
    FROM 
        RankedSalaries 
    GROUP BY 
        company 
    HAVING COUNT(*) % 2 = 0
)

-- Main query to select median salary
SELECT 
    id, 
    company, 
    salary 
FROM 
    RankedSalaries AS rs 
JOIN 
    EvenCountCompanies AS ec USING (company) 
WHERE 
    rs.rank_position IN (ec.employee_count DIV 2, ec.employee_count DIV 2 + 1)

UNION ALL

SELECT 
    id, 
    company, 
    salary 
FROM 
    RankedSalaries AS rs 
JOIN 
    OddCountCompanies AS oc USING (company) 
WHERE 
    rs.rank_position = oc.employee_count DIV 2 + 1;
