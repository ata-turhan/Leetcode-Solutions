WITH RECURSIVE months AS (
    -- Generate months from 1 to 12 for the year 2020
    SELECT 1 AS month
    UNION ALL 
    SELECT month + 1 FROM months
    WHERE month < 12
)
SELECT
    m.month,
    (
        -- Count drivers who joined on or before the last day of each month
        SELECT COUNT(*)
        FROM Drivers d
        WHERE d.join_date <= LAST_DAY(DATE(CONCAT('2020-', LPAD(m.month, 2, '0'), '-01')))
    ) AS active_drivers,
    (
        -- Count rides that were requested within each specific month
        SELECT COUNT(*)
        FROM AcceptedRides ar
        JOIN Rides r ON ar.ride_id = r.ride_id
        WHERE r.requested_at BETWEEN DATE(CONCAT('2020-', LPAD(m.month, 2, '0'), '-01')) 
            AND LAST_DAY(DATE(CONCAT('2020-', LPAD(m.month, 2, '0'), '-01')))
    ) AS accepted_rides
FROM months m
ORDER BY m.month;
