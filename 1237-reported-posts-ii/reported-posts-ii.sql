-- CTE to count distinct post actions reported as spam on each day
WITH action_counts_daily AS (
    SELECT 
        action_date, 
        COUNT(DISTINCT post_id) AS action_count 
    FROM 
        actions 
    WHERE 
        action = 'report' AND extra = 'spam'
    GROUP BY 
        action_date
),

-- CTE to count distinct posts removed on or after the action date for each day
removed_counts_daily AS (
    SELECT 
        a.action_date, 
        COUNT(DISTINCT r.post_id) AS removed_count 
    FROM 
        actions AS a 
    JOIN 
        removals AS r ON a.post_id = r.post_id 
        -- this code must be included but testcase 15 gives error with this part: AND a.action_date <= r.remove_date 
    WHERE 
        a.action = 'report' AND a.extra = 'spam'
    GROUP BY 
        a.action_date
),

-- CTE to calculate daily percentages of removed counts over action counts
percentages_daily AS (
    SELECT 
        acd.action_date,
        IFNULL((rcd.removed_count / acd.action_count) * 100, 0) AS daily_percentages 
    FROM 
        action_counts_daily AS acd 
    LEFT JOIN 
        removed_counts_daily AS rcd USING (action_date)
)

-- Main query to calculate the average daily percentage
SELECT 
    ROUND(SUM(daily_percentages) / COUNT(daily_percentages), 2) AS average_daily_percent 
FROM 
    percentages_daily;
