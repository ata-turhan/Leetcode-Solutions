-- CTE to join flights with passengers and assign a row number to each passenger per flight
WITH flight_passenger_counts AS (
    SELECT 
        f.flight_id, 
        p.passenger_id, 
        f.capacity,
        ROW_NUMBER() OVER (PARTITION BY f.flight_id ORDER BY p.passenger_id ASC) AS rn
    FROM 
        flights AS f 
    LEFT JOIN 
        passengers AS p 
    USING (flight_id)
)

-- Main query to calculate the booked and waitlisted counts for each flight
SELECT 
    flight_id, 
    -- Calculate booked passengers count
    SUM(IF(passenger_id IS NULL, 0, IF(rn <= capacity, 1, 0))) AS booked_cnt, 
    -- Calculate waitlisted passengers count
    SUM(IF(passenger_id IS NULL, 0, IF(rn > capacity, 1, 0))) AS waitlist_cnt 
FROM 
    flight_passenger_counts 
GROUP BY 
    flight_id 
ORDER BY 
    flight_id ASC;
