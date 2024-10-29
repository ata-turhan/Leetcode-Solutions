WITH annual_sales AS (
    -- Summarize total spend for each product per year
    SELECT 
        product_id, 
        YEAR(transaction_date) AS year_val, 
        SUM(spend) AS total_spend 
    FROM 
        user_transactions 
    GROUP BY 
        product_id, year_val
),
yearly_comparison AS (
    -- Calculate the current and previous year spend for each product
    SELECT 
        year_val, 
        product_id, 
        total_spend AS curr_year_spend, 
        LAG(total_spend) OVER (PARTITION BY product_id ORDER BY year_val ASC) AS prev_year_spend 
    FROM 
        annual_sales
)
-- Calculate YoY growth rate and handle potential NULL values in previous year
SELECT 
    year_val AS year, 
    product_id, 
    curr_year_spend, 
    prev_year_spend,
    ROUND((curr_year_spend - prev_year_spend) / prev_year_spend * 100, 2) AS yoy_rate
FROM 
    yearly_comparison;
