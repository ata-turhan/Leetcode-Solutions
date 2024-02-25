# Write your MySQL query statement below
SELECT 
    SUM(b.apple_count + COALESCE(c.apple_count, 0)) AS apple_count,
    SUM(b.orange_count + COALESCE(c.orange_count, 0)) AS orange_count
FROM 
    boxes AS b 
LEFT JOIN 
    chests AS c 
USING 
    (chest_id);
