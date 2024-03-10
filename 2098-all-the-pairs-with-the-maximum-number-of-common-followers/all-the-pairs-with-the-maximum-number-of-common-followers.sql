WITH counts AS (
    SELECT r1.user_id AS u1, r2.user_id AS u2, COUNT(r1.follower_id) AS c 
    FROM relations AS r1 
    JOIN relations AS r2 ON r1.user_id < r2.user_id AND r1.follower_id = r2.follower_id 
    GROUP BY u1, u2
)

SELECT u1 AS user1_id, u2 AS user2_id 
FROM counts 
WHERE c = (SELECT MAX(c) FROM counts);
