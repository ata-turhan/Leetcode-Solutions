WITH joined_listens AS (
    -- Step 1: Join Friendship with Listens to identify common songs listened to by friends on the same day
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
        l1.day = l2.day -- Ensure the listen occurred on the same day
        AND l1.song_id = l2.song_id -- Ensure both friends listened to the same song
),
distinct_songs AS (
    -- Step 2: Count the number of distinct songs listened to by each pair of friends on the same day
    SELECT 
        user1_id, 
        user2_id, 
        day, 
        COUNT(DISTINCT song_id) AS common_songs -- Count only distinct songs
    FROM 
        joined_listens
    GROUP BY 
        user1_id, user2_id, day -- Group by user pair and day to calculate common songs
)
-- Step 3: Filter pairs who listened to at least 3 distinct songs on the same day
SELECT 
    user1_id, 
    user2_id
FROM 
    distinct_songs
WHERE 
    common_songs >= 3 -- Only include pairs with at least 3 common songs
GROUP BY 
    user1_id, user2_id; -- Ensure unique pairs in the result
