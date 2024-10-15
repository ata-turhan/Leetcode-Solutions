WITH all_friends AS (
    -- Get all combinations of friendships by unioning user1 and user2 in both directions
    SELECT user1, user2 FROM friends 
    UNION ALL
    SELECT user2 AS user1, user1 AS user2 FROM friends
),
friends_count AS (
    -- Count distinct friends for each user
    SELECT user1, COUNT(DISTINCT user2) AS friends_count 
    FROM all_friends 
    GROUP BY user1
),
total_users AS (
    -- Calculate the total number of distinct users
    SELECT COUNT(DISTINCT user1) AS total_user_count 
    FROM all_friends
)
-- Calculate popularity as a percentage of total users, ordered by user1
SELECT 
    fc.user1,
    ROUND(100 * fc.friends_count / tu.total_user_count, 2) AS percentage_popularity
FROM 
    friends_count fc, total_users tu
ORDER BY 
    fc.user1 ASC;
