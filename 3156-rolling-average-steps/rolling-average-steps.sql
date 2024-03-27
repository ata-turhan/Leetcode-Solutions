WITH StepsWithLag AS (
    SELECT 
        user_id,
        steps_date,
        ROUND(AVG(steps_count) OVER (PARTITION BY user_id ORDER BY steps_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS rolling_average,
        LAG(steps_date, 2) OVER (PARTITION BY user_id ORDER BY steps_date) AS lag_date
    FROM 
        steps
)
SELECT 
    user_id,
    steps_date,
    rolling_average
FROM 
    StepsWithLag
WHERE
    DATEDIFF(steps_date, lag_date) = 2
ORDER BY 
    user_id, 
    steps_date;
