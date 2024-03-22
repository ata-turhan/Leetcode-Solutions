SELECT 
    age_bucket,
    ROUND(100 * SUM(IF(activity_type = "send", 1, 0) * time_spent) / SUM(time_spent), 2) AS send_perc,
    ROUND(100 * SUM(IF(activity_type = "open", 1, 0) * time_spent) / SUM(time_spent), 2) AS open_perc
FROM 
    activities 
JOIN 
    age USING (user_id) 
GROUP BY 
    age_bucket;
