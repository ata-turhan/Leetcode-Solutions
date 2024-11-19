WITH senior_candidates AS (
    -- Calculate cumulative salary for Senior candidates ordered by salary in ascending order
    SELECT 
        SUM(salary) OVER (ORDER BY salary ASC) AS cumulative_salary
    FROM candidates 
    WHERE experience = "Senior"
),
hired_seniors_summary AS (
    -- Get the count of accepted senior candidates and their total cost
    SELECT 
        COUNT(*) AS accepted_candidates, 
        IFNULL(MAX(cumulative_salary), 0) AS total_senior_cost
    FROM senior_candidates
    WHERE cumulative_salary <= 70000
),
junior_candidates AS (
    -- Calculate cumulative salary for Junior candidates ordered by salary in ascending order
    SELECT 
        SUM(salary) OVER (ORDER BY salary ASC) AS cumulative_salary
    FROM candidates 
    WHERE experience = "Junior"
),
hired_juniors_summary AS (
    -- Get the count of accepted junior candidates within the remaining budget
    SELECT 
        COUNT(*) AS accepted_candidates
    FROM junior_candidates
    WHERE cumulative_salary <= (70000 - (SELECT total_senior_cost FROM hired_seniors_summary))
)
-- Combine results for both Senior and Junior candidates
SELECT 
    "Senior" AS experience, 
    accepted_candidates 
FROM hired_seniors_summary
UNION ALL
SELECT 
    "Junior" AS experience, 
    accepted_candidates 
FROM hired_juniors_summary;
