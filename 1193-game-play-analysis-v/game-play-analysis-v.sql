WITH activity_ranked AS (
    SELECT 
        event_date, 
        RANK() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS day_rank,
        LEAD(event_date) OVER (PARTITION BY player_id ORDER BY event_date ASC) AS next_date
    FROM activity
),
dates_retention_calculated AS (
    SELECT 
        event_date, 
        CASE WHEN DATEDIFF(next_date, event_date) = 1 THEN 1 ELSE 0 END AS has_retention
    FROM activity_ranked
    WHERE day_rank = 1
)
SELECT 
    event_date AS install_dt, 
    COUNT(event_date) AS installs, 
    ROUND(AVG(has_retention), 2) AS Day1_retention
FROM 
    dates_retention_calculated
GROUP BY 
    event_date;
