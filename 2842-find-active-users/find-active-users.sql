-- CTE to assign row numbers to each user's creation dates, ordered by the creation date
WITH users_dates AS (
    SELECT 
        user_id, 
        created_at, 
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at ASC) AS rn
    FROM 
        users
),

-- CTE to pair each user's creation dates with the subsequent creation date
users_dates_next_dates AS (
    SELECT 
        us1.user_id, 
        us1.created_at AS prev_date, 
        us2.created_at AS next_date
    FROM 
        users_dates AS us1
    JOIN 
        users_dates AS us2 
    ON 
        us1.user_id = us2.user_id 
        AND us1.rn + 1 = us2.rn
)

-- Main query to find users with consecutive creation dates within 7 days
SELECT 
    DISTINCT user_id 
FROM 
    users_dates_next_dates 
WHERE 
    DATEDIFF(next_date, prev_date) <= 7;
