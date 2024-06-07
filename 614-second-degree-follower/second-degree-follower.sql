-- CTE to find second-degree followers
WITH second_degree_followers AS (
    SELECT DISTINCT f1.followee AS person
    FROM follow AS f1
    JOIN follow AS f2 ON f1.followee = f2.follower
)

-- Main query to count the number of followers for each second-degree follower
SELECT 
    followee AS follower, 
    COUNT(follower) AS num
FROM 
    follow
WHERE 
    followee IN (SELECT person FROM second_degree_followers)
GROUP BY 
    followee
ORDER BY 
    follower ASC;
