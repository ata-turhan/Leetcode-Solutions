WITH all_pairs AS (
    SELECT user1_id, user2_id FROM Friendship
    UNION
    SELECT user2_id, user1_id FROM Friendship
),
common_friends_count AS (
    SELECT f1.user1_id, f1.user2_id, COUNT(f3.user2_id) AS common_friend 
    FROM Friendship AS f1
    JOIN all_pairs AS f2 ON f1.user1_id = f2.user1_id AND f1.user2_id != f2.user2_id 
    JOIN all_pairs AS f3 ON f1.user2_id = f3.user1_id AND f2.user2_id = f3.user2_id 
    GROUP BY f1.user1_id, f1.user2_id
)
SELECT user1_id, user2_id, common_friend 
FROM common_friends_count 
WHERE common_friend >= 3;
