-- CTE to get distinct login dates for each user
WITH DistinctLogins AS (
    SELECT DISTINCT
        id,
        login_date
    FROM 
        Logins
),

-- CTE to calculate the streaks of consecutive login days for each user
LoginStreaks AS (
    SELECT
        id,
        login_date,
        COUNT(*) OVER (
            PARTITION BY id 
            ORDER BY login_date 
            RANGE BETWEEN INTERVAL 4 DAY PRECEDING AND CURRENT ROW
        ) AS streak
    FROM
        DistinctLogins
),

-- CTE to find users with a login streak of 5 or more consecutive days
ActiveUsers AS (
    SELECT DISTINCT
        id
    FROM 
        LoginStreaks
    WHERE 
        streak >= 5
)

-- Main query to get the id and name of active users
SELECT 
    a.id, 
    a.name
FROM 
    Accounts AS a
JOIN 
    ActiveUsers AS au
ON 
    a.id = au.id
ORDER BY 
    a.id;
