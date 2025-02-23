WITH friends AS (
    SELECT requester_id AS r FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS r FROM RequestAccepted
)
SELECT r AS id, COUNT(*) AS num
FROM friends
GROUP BY r
ORDER BY num DESC
LIMIT 1;
