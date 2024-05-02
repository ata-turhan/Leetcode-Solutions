WITH ranks_tx AS (
    SELECT 
        *,
        RANK() OVER (PARTITION BY user_id ORDER BY transaction_date ASC) AS ranks
    FROM 
        Transactions
)
SELECT 
    r1.user_id,
    r1.spend AS third_transaction_spend,
    r1.transaction_date AS third_transaction_date
FROM 
    ranks_tx AS r1
LEFT JOIN 
    ranks_tx AS r2 ON r1.ranks = 3 AND r1.ranks - 1 = r2.ranks AND r1.user_id = r2.user_id
LEFT JOIN 
    ranks_tx AS r3 ON r2.ranks - 1 = r3.ranks AND r1.user_id = r3.user_id
WHERE 
    r1.spend > r2.spend 
    AND r1.spend > r3.spend;
