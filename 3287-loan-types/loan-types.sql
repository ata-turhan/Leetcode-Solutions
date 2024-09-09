-- Query to select users who have both "Refinance" and "Mortgage" loan types
SELECT 
    user_id 
FROM 
    loans 
GROUP BY 
    user_id 
HAVING 
    SUM(loan_type = 'Refinance') > 0  -- Check if the user has at least one "Refinance" loan
    AND SUM(loan_type = 'Mortgage') > 0  -- Check if the user has at least one "Mortgage" loan
ORDER BY 
    user_id ASC;  -- Order the result by user_id in ascending order
