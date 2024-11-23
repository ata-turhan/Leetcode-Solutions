WITH joined_listens AS (
    SELECT 
        f.user1_id, 
        f.user2_id, 
        l1.day, 
        l1.song_id
    FROM 
        Friendship f
    JOIN 
        Listens l1 ON f.user1_id = l1.user_id
    JOIN 
        Listens l2 ON f.user2_id = l2.user_id
    WHERE 
        l1.day = l2.day AND l1.song_id = l2.song_id
),
distinct_songs AS (
    SELECT 
        user1_id, 
        user2_id, 
        day, 
        COUNT(DISTINCT song_id) AS common_songs
    FROM 
        joined_listens
    GROUP BY 
        user1_id, user2_id, day
)
SELECT 
    user1_id, 
    user2_id
FROM 
    distinct_songs
WHERE 
    common_songs >= 3
GROUP BY 
    user1_id, user2_id;
