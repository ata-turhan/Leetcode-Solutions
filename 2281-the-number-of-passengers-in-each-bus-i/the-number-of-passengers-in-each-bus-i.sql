-- CTE to assign row numbers to bus arrivals in ascending order of arrival time
WITH bus_orders AS (
    SELECT 
        bus_id, 
        arrival_time, 
        ROW_NUMBER() OVER (ORDER BY arrival_time ASC) AS rn 
    FROM 
        buses
),
-- CTE to calculate the interval between consecutive bus arrivals
bus_intervals AS (
    SELECT 
        b1.bus_id, 
        b1.arrival_time, 
        COALESCE(b2.arrival_time, -1) AS prev_arrival_time 
    FROM 
        bus_orders AS b1 
    LEFT JOIN 
        bus_orders AS b2 
    ON 
        b1.rn = b2.rn + 1
)
-- Query to count the number of passengers for each bus based on arrival times
SELECT 
    bus_id, 
    COUNT(passenger_id) AS passengers_cnt  
FROM 
    bus_intervals 
LEFT JOIN 
    passengers 
ON 
    bus_intervals.prev_arrival_time < passengers.arrival_time 
    AND passengers.arrival_time <= bus_intervals.arrival_time 
GROUP BY 
    bus_id 
ORDER BY 
    bus_id ASC;
