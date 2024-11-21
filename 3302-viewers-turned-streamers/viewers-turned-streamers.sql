WITH RankedSessions AS (
    SELECT 
        *,
        RANK() OVER (PARTITION BY user_id ORDER BY session_start ASC) AS session_rank
    FROM sessions
),
FirstViewers AS (
    SELECT 
        user_id
    FROM 
        RankedSessions
    WHERE 
        session_rank = 1 
        AND session_type = 'Viewer'
)
SELECT 
    s.user_id, 
    SUM(CASE WHEN s.session_type = 'Streamer' THEN 1 ELSE 0 END) AS sessions_count 
FROM 
    sessions s
JOIN 
    FirstViewers fv
USING 
    (user_id)
GROUP BY 
    s.user_id
HAVING 
    sessions_count > 0
ORDER BY 
    sessions_count  DESC, 
    s.user_id DESC;
