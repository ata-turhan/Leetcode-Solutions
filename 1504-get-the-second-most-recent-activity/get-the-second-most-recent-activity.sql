-- CTE to rank activities for each user based on the end date
WITH UserActivityRanks AS (
    SELECT 
        username,
        activity,
        startDate,
        endDate,
        RANK() OVER (PARTITION BY username ORDER BY endDate DESC) AS ranking
    FROM 
        useractivity
),

-- CTE to select users with only one activity
SingleActivityUsers AS (
    SELECT 
        username,
        activity,
        startDate,
        endDate
    FROM 
        useractivity
    GROUP BY 
        username
    HAVING 
        COUNT(*) = 1
)

-- Main query to select the second latest activity and all single activities
SELECT 
    username, 
    activity, 
    startDate, 
    endDate
FROM 
    UserActivityRanks 
WHERE 
    ranking = 2

UNION ALL 

SELECT 
    username, 
    activity, 
    startDate, 
    endDate
FROM 
    SingleActivityUsers;
