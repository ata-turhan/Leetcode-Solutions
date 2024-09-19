-- Select the score and calculate the dense rank for each score
-- using the DENSE_RANK() function to ensure that identical scores get the same rank
-- and no gaps in ranking for identical scores
SELECT 
    score, 
    DENSE_RANK() OVER (ORDER BY score DESC) AS "rank"
FROM 
    scores
-- Order the result by score in descending order to match the ranking
ORDER BY 
    score DESC;
