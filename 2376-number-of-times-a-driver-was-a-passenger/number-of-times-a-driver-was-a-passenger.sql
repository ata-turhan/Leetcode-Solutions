WITH unique_drivers AS (
    SELECT DISTINCT driver_id AS ddi FROM rides
)
SELECT r1.ddi AS driver_id, COUNT(r2.passenger_id) AS cnt 
FROM unique_drivers AS r1 
LEFT JOIN rides AS r2 ON r1.ddi = r2.passenger_id 
GROUP BY r1.ddi;
