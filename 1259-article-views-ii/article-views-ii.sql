-- Select viewer IDs from the "views" table
SELECT 
    DISTINCT viewer_id AS id -- Alias viewer_id as id
FROM 
    views 
-- Group the results by view date and viewer ID
GROUP BY 
    view_date, 
    viewer_id 
-- Filter the groups where the count of distinct article IDs is greater than 1
HAVING 
    COUNT(DISTINCT article_id) > 1 
-- Order the results by viewer ID in ascending order
ORDER BY 
    viewer_id ASC;
