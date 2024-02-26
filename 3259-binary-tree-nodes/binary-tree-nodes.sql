SELECT N,
    CASE
        WHEN p IS NULL THEN 'Root'
        WHEN n IN (SELECT p FROM tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM tree
ORDER BY N;
