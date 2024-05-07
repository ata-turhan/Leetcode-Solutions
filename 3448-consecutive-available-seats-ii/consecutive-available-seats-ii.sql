-- Assign row numbers to free seats in the cinema
WITH cinema_with_rn AS (
    SELECT 
        seat_id, 
        ROW_NUMBER() OVER (PARTITION BY free ORDER BY seat_id ASC) AS rn 
    FROM 
        cinema 
    WHERE 
        free = 1
),
-- Calculate consecutive groups of free seats
consecutive_groups AS (
    SELECT 
        MIN(seat_id) AS first_seat_id, 
        MAX(seat_id) AS last_seat_id, 
        COUNT(*) AS consecutive_seats_len  
    FROM 
        cinema_with_rn 
    GROUP BY 
        seat_id - rn
)
-- Select consecutive groups with the maximum number of consecutive seats
SELECT 
    * 
FROM 
    consecutive_groups 
WHERE 
    consecutive_seats_len = (
        SELECT 
            MAX(consecutive_seats_len) 
        FROM 
            consecutive_groups
    ) 
ORDER BY 
    first_seat_id ASC;
