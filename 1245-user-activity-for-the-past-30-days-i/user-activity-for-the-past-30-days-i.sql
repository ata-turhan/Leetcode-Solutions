-- Count distinct active users within the last 30 days before "2019-07-27"
SELECT 
    activity_date AS day, 
    COUNT(DISTINCT user_id) AS active_users
FROM 
    activity
WHERE 
    activity_date BETWEEN DATE_SUB("2019-07-27", INTERVAL 29 DAY) AND DATE_SUB("2019-07-27", INTERVAL 0 DAY)
GROUP BY 
    activity_date
ORDER BY 
    activity_date;
