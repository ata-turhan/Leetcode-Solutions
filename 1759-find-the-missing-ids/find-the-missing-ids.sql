WITH RECURSIVE id_table AS (
    SELECT 1 AS ids
    UNION 
    SELECT ids + 1
    FROM id_table
    WHERE ids < (SELECT MAX(customer_id) FROM Customers)
    LIMIT 100
)
SELECT ids
FROM id_table
WHERE ids NOT IN (SELECT customer_id FROM Customers);