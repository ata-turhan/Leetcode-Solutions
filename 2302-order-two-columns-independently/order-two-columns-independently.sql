-- Create common table expressions (CTEs) to assign row numbers based on the ordering of first_col and second_col
WITH first_col_ranks AS (
    SELECT 
        first_col, 
        ROW_NUMBER() OVER(ORDER BY first_col ASC) AS first_col_row_num -- Assign row numbers based on ascending order of first_col
    FROM 
        Data
),
second_col_ranks AS (
    SELECT 
        second_col, 
        ROW_NUMBER() OVER(ORDER BY second_col DESC) AS second_col_row_num -- Assign row numbers based on descending order of second_col
    FROM 
        Data
)

-- Join the CTEs based on matching row numbers to retrieve corresponding columns
SELECT 
    first_col_ranks.first_col, -- Select the first column from the first CTE
    second_col_ranks.second_col -- Select the second column from the second CTE
FROM 
    first_col_ranks -- Alias for the first CTE
JOIN 
    second_col_ranks -- Alias for the second CTE
ON 
    first_col_ranks.first_col_row_num = second_col_ranks.second_col_row_num; -- Join based on matching row numbers
