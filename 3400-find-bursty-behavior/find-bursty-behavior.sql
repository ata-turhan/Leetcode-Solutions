-- CTE to filter posts from February 2024
WITH FebruaryPosts AS (
    SELECT 
        * 
    FROM 
        Posts 
    WHERE 
        post_date BETWEEN '2024-02-01' AND '2024-02-28'
),

-- CTE to calculate the average weekly posts for each user in February 2024
AvgWeeklyPosts AS (
    SELECT 
        user_id, 
        COUNT(*) / 4.0 AS avg_weekly_posts  -- February has exactly 4 weeks
    FROM 
        FebruaryPosts 
    GROUP BY 
        user_id
),

-- CTE to calculate the number of posts in any 7-day window for each user
SevenDayPostCount AS (
    SELECT 
        user_id, 
        post_date, 
        COUNT(*) OVER (
            PARTITION BY user_id 
            ORDER BY post_date 
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
        ) AS posts_in_7_days
    FROM 
        FebruaryPosts
),

-- CTE to find the maximum number of posts in any 7-day window for each user
MaxSevenDayPostCount AS (
    SELECT 
        user_id, 
        MAX(posts_in_7_days) AS max_7day_posts
    FROM 
        SevenDayPostCount
    GROUP BY 
        user_id
),

-- CTE to identify users with bursty behavior
BurstyUsers AS (
    SELECT 
        m.user_id, 
        m.max_7day_posts, 
        a.avg_weekly_posts
    FROM 
        MaxSevenDayPostCount m
    INNER JOIN 
        AvgWeeklyPosts a USING (user_id)
    HAVING 
        m.max_7day_posts >= 2 * a.avg_weekly_posts
)

-- Final query to select bursty users ordered by user_id
SELECT 
    user_id, 
    max_7day_posts, 
    ROUND(avg_weekly_posts, 4) AS avg_weekly_posts
FROM 
    BurstyUsers
ORDER BY 
    user_id;
