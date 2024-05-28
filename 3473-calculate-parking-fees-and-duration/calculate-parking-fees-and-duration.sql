-- CTE to calculate the duration in hours for each parking transaction
WITH ParkingDurations AS (
    SELECT 
        car_id,
        lot_id,
        fee_paid,
        -- Calculate the duration in hours by finding the difference between entry and exit times
        TIMESTAMPDIFF(MINUTE, entry_time, exit_time) / 60.0 AS duration_hours
    FROM 
        ParkingTransactions
),

-- CTE to calculate the total fee paid and total duration in hours for each car
TotalFees AS (
    SELECT 
        car_id,
        SUM(fee_paid) AS total_fee_paid,
        SUM(duration_hours) AS total_hours
    FROM 
        ParkingDurations
    GROUP BY 
        car_id
),

-- CTE to calculate the total duration in hours each car spent in each parking lot
LotDurations AS (
    SELECT 
        car_id,
        lot_id,
        SUM(duration_hours) AS lot_total_hours
    FROM 
        ParkingDurations
    GROUP BY 
        car_id, lot_id
),

-- CTE to find the parking lot where each car spent the most time
MaxTimeLot AS (
    SELECT 
        car_id,
        lot_id AS most_time_lot,
        lot_total_hours,
        -- Rank lots by total duration in descending order for each car
        RANK() OVER (PARTITION BY car_id ORDER BY lot_total_hours DESC) AS rnk
    FROM 
        LotDurations
)

-- Main query to select the final results
SELECT 
    tf.car_id,
    tf.total_fee_paid,
    -- Calculate the average hourly fee and round it to 2 decimal places
    ROUND(tf.total_fee_paid / tf.total_hours, 2) AS avg_hourly_fee,
    mtl.most_time_lot
FROM 
    TotalFees tf
JOIN 
    -- Join with the CTE to get the lot where each car spent the most time
    (SELECT car_id, most_time_lot FROM MaxTimeLot WHERE rnk = 1) mtl ON tf.car_id = mtl.car_id
ORDER BY 
    tf.car_id;  -- Order by car_id in ascending order
