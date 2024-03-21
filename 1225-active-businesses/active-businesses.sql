WITH average_activity AS (
    SELECT event_type, AVG(occurrences) AS average_occurrence 
    FROM events 
    GROUP BY event_type
)
SELECT e.business_id 
FROM events AS e 
JOIN average_activity AS a USING(event_type) 
WHERE occurrences > average_occurrence 
GROUP BY business_id 
HAVING COUNT(*) > 1;
