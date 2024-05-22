WITH coordinates_with_rn AS (
    SELECT x, y, ROW_NUMBER() OVER () AS rn
    FROM Coordinates
)

-- Main query to find symmetric pairs and ensure x <= y
SELECT DISTINCT
    c1.x, c1.y
FROM 
    coordinates_with_rn AS c1
JOIN 
    coordinates_with_rn AS c2
ON 
    c1.x = c2.y AND c1.y = c2.x AND c1.rn != c2.rn
WHERE 
    c1.x <= c1.y
ORDER BY 
    c1.x, c1.y;
