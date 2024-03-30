WITH GoldMedals AS (
    SELECT 
        user_id 
    FROM 
        users 
    JOIN 
        contests ON user_id = gold_medal 
    GROUP BY 
        user_id 
    HAVING 
        COUNT(contest_id) >= 3 
),
AllMedals AS (
    SELECT 
        user_id, 
        contest_id AS cur, 
        LAG(contest_id, 1) OVER (PARTITION BY user_id ORDER BY contest_id) AS prev, 
        LEAD(contest_id, 1) OVER (PARTITION BY user_id ORDER BY contest_id) AS next
    FROM 
        users 
    JOIN 
        contests ON user_id = gold_medal OR user_id = silver_medal OR user_id = bronze_medal
),
ConsecutiveMedals AS (
    SELECT 
        DISTINCT user_id 
    FROM 
        AllMedals 
    WHERE 
        cur = prev + 1 AND cur = next - 1
)
SELECT 
    name, 
    mail 
FROM 
    users 
WHERE 
    user_id IN (
        SELECT 
            user_id 
        FROM 
            GoldMedals
        UNION
        SELECT 
            user_id 
        FROM 
            ConsecutiveMedals
    );
