-- Common Table Expression (CTE) to generate row numbers for the CoffeeShop table
WITH RECURSIVE CoffeeShopRowNum AS (
    -- Assign a unique row number to each row in the CoffeeShop table
    SELECT
        ROW_NUMBER() OVER() AS row_num,
        id,
        drink
    FROM 
        CoffeeShop
), 
-- Recursive CTE to fill in NULL values in the "drink" column with the previous non-NULL value
Result AS (
    -- Base case: Select the first row from CoffeeShopRowNum
    SELECT
        row_num,
        id,
        drink
    FROM 
        CoffeeShopRowNum
    WHERE 
        row_num = 1
    UNION ALL
    -- Recursive step: Fill in NULL values in the "drink" column with the previous non-NULL value
    SELECT
        CSRN.row_num,
        CSRN.id,
        COALESCE(CSRN.drink, R.drink) AS drink
    FROM 
        Result AS R
    JOIN 
        CoffeeShopRowNum AS CSRN ON R.row_num = CSRN.row_num - 1
)
-- Final SELECT statement to retrieve the results
SELECT 
    id, 
    drink
FROM 
    Result;
