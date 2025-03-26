SELECT 
    e1.name
FROM employee AS e1
JOIN employee AS e2 
    ON e1.id = e2.managerId
GROUP BY e1.id, e1.name
HAVING COUNT(*) >= 5;
