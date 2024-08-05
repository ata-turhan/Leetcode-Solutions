-- CTE to generate all months from 1 to 12
WITH RECURSIVE AllMonths AS (
    SELECT 1 AS month
    UNION
    SELECT month + 1 FROM AllMonths
    WHERE month < 12
),

-- CTE to calculate the ride distance and duration for each month in 2020
MonthlyRides AS (
    SELECT 
        MONTH(r.requested_at) AS month, 
        SUM(a.ride_distance) AS ride_distance, 
        SUM(a.ride_duration) AS ride_duration
    FROM 
        Rides AS r
    JOIN 
        AcceptedRides AS a ON r.ride_id = a.ride_id
    WHERE 
        YEAR(r.requested_at) = 2020
    GROUP BY 
        MONTH(r.requested_at)
),

-- CTE to ensure all months are included with default values for months with no data
MonthlyRidesFull AS (
    SELECT 
        am.month, 
        COALESCE(mr.ride_distance, 0) AS ride_distance,
        COALESCE(mr.ride_duration, 0) AS ride_duration
    FROM 
        AllMonths AS am
    LEFT JOIN 
        MonthlyRides AS mr ON am.month = mr.month
),

-- CTE to calculate the 3-month rolling averages
RollingAverages AS (
    SELECT 
        month,
        AVG(ride_distance) OVER (ORDER BY month ASC ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING) AS average_ride_distance,
        AVG(ride_duration) OVER (ORDER BY month ASC ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING) AS average_ride_duration
    FROM 
        MonthlyRidesFull
)

-- Main query to select and format the results, excluding the last two months
SELECT 
    month, 
    ROUND(average_ride_distance, 2) AS average_ride_distance,
    ROUND(average_ride_duration, 2) AS average_ride_duration
FROM 
    RollingAverages
WHERE 
    month NOT IN (11, 12)
ORDER BY 
    month;
