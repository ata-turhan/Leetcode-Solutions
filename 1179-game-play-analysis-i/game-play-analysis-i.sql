-- Select player_id and the minimum event_date to find the first login date for each player
SELECT 
    player_id, 
    MIN(event_date) AS first_login
FROM 
    activity
-- Group by player_id to get the first login for each player
GROUP BY 
    player_id;
