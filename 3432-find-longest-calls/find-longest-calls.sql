-- Rank the durations of calls by type
WITH rank_orders AS (
    SELECT 
        first_name, 
        type, 
        duration,
        RANK() OVER (PARTITION BY type ORDER BY duration DESC) AS dur_ranks -- Rank the durations for each type
    FROM 
        contacts AS co 
    JOIN 
        calls AS ca ON co.id = ca.contact_id
)

-- Select the top 3 durations for each type and format them into HH:MM:SS
SELECT 
    first_name, 
    type, 
    CONCAT(
        LPAD(FLOOR(duration / 3600), 2, '0'), ':', -- Hours
        LPAD(FLOOR((duration % 3600) / 60), 2, '0'), ':', -- Minutes
        LPAD(duration % 60, 2, '0') -- Seconds
    ) AS duration_formatted -- Format duration into HH:MM:SS
FROM 
    rank_orders 
WHERE 
    dur_ranks <= 3 -- Select only the top 3 durations for each type
ORDER BY 
    type, 
    duration_formatted DESC, -- Order by duration in descending order
    first_name DESC; -- Then by first name in descending order
