-- CTE to assign a row number to each passenger based on booking time for each flight
WITH PassengerBookingOrder AS (
    SELECT 
        p.passenger_id, 
        p.booking_time, 
        f.flight_id, 
        f.capacity, 
        ROW_NUMBER() OVER (PARTITION BY f.flight_id ORDER BY p.booking_time) AS booking_order 
    FROM 
        passengers AS p 
    JOIN 
        flights AS f USING (flight_id) 
)

-- Main query to determine the status of each passenger
SELECT 
    passenger_id, 
    IF(booking_order <= capacity, 'Confirmed', 'Waitlist') AS STATUS 
FROM 
    PassengerBookingOrder 
ORDER BY 
    passenger_id;
