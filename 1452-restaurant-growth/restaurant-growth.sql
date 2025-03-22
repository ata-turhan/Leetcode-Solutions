SELECT 
    visited_on, 
    amount, 
    ROUND(amount / 7, 2) AS average_amount
FROM (
    SELECT 
        DISTINCT visited_on,
        -- Rolling 7-day sum ending on each visited_on
        SUM(amount) OVER (
            ORDER BY visited_on 
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
        ) AS amount,
        
        -- First available visited_on date
        MIN(visited_on) OVER () AS first_date
    FROM Customer
) AS t
WHERE visited_on >= DATE_ADD(first_date, INTERVAL 6 DAY);
