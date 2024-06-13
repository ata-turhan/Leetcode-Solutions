-- Main query to find candidate IDs who have skills in Python, Tableau, and PostgreSQL
SELECT 
    c1.candidate_id 
FROM 
    candidates AS c1 
JOIN 
    candidates AS c2 
ON 
    c1.candidate_id = c2.candidate_id 
    AND c1.skill = 'Python' 
    AND c2.skill = 'Tableau' 
JOIN 
    candidates AS c3 
ON 
    c1.candidate_id = c3.candidate_id 
    AND c3.skill = 'PostgreSQL' 
ORDER BY 
    c1.candidate_id ASC;
