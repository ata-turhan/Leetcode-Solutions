SELECT DISTINCT 
    l1.num AS ConsecutiveNums
FROM logs l1
JOIN logs l2 ON l1.id = l2.id + 1
JOIN logs l3 ON l2.id = l3.id + 1
WHERE 
    l1.num = l2.num AND 
    l2.num = l3.num;
