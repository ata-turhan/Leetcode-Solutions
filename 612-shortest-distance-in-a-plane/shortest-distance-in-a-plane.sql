SELECT 
    MIN(ROUND(POWER(POWER((p1.x - p2.x), 2) + POWER((p1.y - p2.y), 2), 0.5), 2)) AS shortest 
FROM 
    point2d AS p1
JOIN 
    point2d AS p2 
ON 
    (p1.x != p2.x OR p1.y != p2.y);
