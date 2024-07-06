-- CTE to generate all dates in November 2023
WITH RECURSIVE AllDates AS (
    SELECT '2023-11-01' AS purchase_date
    UNION ALL
    SELECT DATE_ADD(purchase_date, INTERVAL 1 DAY)
    FROM AllDates
    WHERE purchase_date < '2023-11-30'
),

-- CTE to filter only Fridays and calculate the week of the month
Fridays AS (
    SELECT 
        purchase_date,
        WEEK(purchase_date, 1) - WEEK(DATE_SUB(purchase_date, INTERVAL DAYOFMONTH(purchase_date) - 1 DAY), 1) + 1 AS week_of_month
    FROM 
        AllDates
    WHERE 
        DAYOFWEEK(purchase_date) = 6
),

-- CTE to calculate the total spending on each Friday
FridayPurchases AS (
    SELECT 
        f.week_of_month,
        f.purchase_date,
        COALESCE(SUM(p.amount_spend), 0) AS total_amount
    FROM 
        Fridays AS f
    LEFT JOIN 
        Purchases AS p ON f.purchase_date = p.purchase_date
    GROUP BY 
        f.week_of_month, f.purchase_date
)

-- Main query to select and order the results
SELECT 
    week_of_month,
    purchase_date,
    total_amount
FROM 
    FridayPurchases
ORDER BY 
    week_of_month ASC;
