WITH counts AS (
    SELECT activity, COUNT(*) AS c 
    FROM friends 
    GROUP BY activity
),
ext AS (
    SELECT activity 
    FROM counts 
    WHERE c = (SELECT MAX(c) FROM counts) 
    UNION 
    SELECT activity 
    FROM counts 
    WHERE c = (SELECT MIN(c) FROM counts)
)

SELECT name AS activity 
FROM activities 
WHERE name NOT IN (SELECT activity FROM ext);
