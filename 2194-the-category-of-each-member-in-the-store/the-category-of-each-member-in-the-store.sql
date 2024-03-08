SELECT 
    m.member_id, 
    m.name, 
    CASE
        WHEN (100 * COUNT(p.visit_id) / COUNT(v.visit_id)) >= 80 THEN 'Diamond'
        WHEN (100 * COUNT(p.visit_id) / COUNT(v.visit_id)) BETWEEN 50 AND 79 THEN 'Gold'
        WHEN (100 * COUNT(p.visit_id) / COUNT(v.visit_id)) < 50 THEN 'Silver'
        WHEN COUNT(v.visit_id) = 0 THEN 'Bronze'
    END AS category
FROM 
    members AS m
LEFT JOIN 
    visits AS v USING (member_id)
LEFT JOIN 
    purchases AS p USING (visit_id)
GROUP BY 
    m.member_id
ORDER BY 
    m.member_id;
