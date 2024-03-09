WITH counts AS (
    SELECT departure_airport AS airport, flights_count FROM flights
    UNION ALL
    SELECT arrival_airport AS airport, flights_count FROM flights
),
grpd_counts AS (
    SELECT airport, SUM(flights_count) AS total_flights FROM counts GROUP BY airport
)
SELECT airport AS airport_id 
FROM grpd_counts 
WHERE total_flights = (SELECT MAX(total_flights) FROM grpd_counts);
