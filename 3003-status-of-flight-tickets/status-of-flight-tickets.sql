-- CTE to assign a row number to each passenger based on booking time for each flight
WITH passenger_order AS (
    SELECT 
        p.passenger_id, 
        p.booking_time, 
        f.flight_id, 
        f.capacity, 
        ROW_NUMBER() OVER (PARTITION BY f.flight_id ORDER BY p.booking_time) AS passenger_number 
    FROM 
        passengers AS p 
    JOIN 
        flights AS f USING (flight_id) 
)

-- Main query to determine the status of each passenger
SELECT 
    passenger_id, 
    IF(passenger_number <= capacity, 'Confirmed', 'Waitlist') AS Status 
FROM 
    passenger_order 
ORDER BY 
    passenger_id;
