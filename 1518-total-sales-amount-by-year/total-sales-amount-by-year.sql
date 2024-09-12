-- Step 1: Define the sales_years CTE to create year ranges for reporting
WITH sales_years AS (
    SELECT
        '2018' AS report_year,
        CAST('2018-01-01' AS DATE) AS year_start,
        CAST('2018-12-31' AS DATE) AS year_end
    UNION ALL
    SELECT
        '2019' AS report_year,
        CAST('2019-01-01' AS DATE) AS year_start,
        CAST('2019-12-31' AS DATE) AS year_end
    UNION ALL
    SELECT
        '2020' AS report_year,
        CAST('2020-01-01' AS DATE) AS year_start,
        CAST('2020-12-31' AS DATE) AS year_end
)

-- Step 2: Query to calculate total sales for each product in each year
SELECT
    s.product_id,  -- Product ID
    p.product_name,  -- Product name
    y.report_year,  -- Reporting year from sales_years CTE
    SUM(
        -- Calculate total sales using the days between start and end periods 
        (DATEDIFF(LEAST(s.period_end, y.year_end), GREATEST(s.period_start, y.year_start)) + 1) * s.average_daily_sales
    ) AS total_amount
FROM
    Sales s
JOIN 
    Product p ON s.product_id = p.product_id  -- Join Sales with Product to get product name
JOIN 
    sales_years y ON y.report_year BETWEEN YEAR(s.period_start) AND YEAR(s.period_end)  -- Join with sales_years for overlapping years
GROUP BY
    s.product_id, p.product_name, y.report_year  -- Group by product ID, name, and report year
ORDER BY
    s.product_id, y.report_year;  -- Order by product ID and report year for clarity
