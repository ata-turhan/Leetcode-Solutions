WITH RECURSIVE months AS (
    SELECT 1 AS month
    UNION ALL 
    SELECT month + 1 from months
    where month < 12
)
SELECT
    m.month,
    (
        SELECT COUNT(*)
        FROM Drivers d
        WHERE d.join_date <= LAST_DAY(DATE(CONCAT('2020-', LPAD(m.month, 2, '0'), '-01')))
    ) AS active_drivers,
    (
        SELECT COUNT(*)
        FROM AcceptedRides ar
        JOIN Rides r ON ar.ride_id = r.ride_id
        WHERE r.requested_at >= DATE(CONCAT('2020-', LPAD(m.month, 2, '0'), '-01'))
          AND r.requested_at <= LAST_DAY(DATE(CONCAT('2020-', LPAD(m.month, 2, '0'), '-01')))
    ) AS accepted_rides
FROM months m
ORDER BY m.month;
