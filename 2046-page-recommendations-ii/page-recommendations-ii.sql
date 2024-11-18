WITH all_friends AS (
    -- Create a bidirectional friendship relationship
    SELECT user1_id AS user_id, user2_id AS friend_id
    FROM friendship
    UNION ALL
    SELECT user2_id AS user_id, user1_id AS friend_id
    FROM friendship
)
SELECT 
    af.user_id AS user_id,            -- The user ID
    l1.page_id AS page_id,           -- The page ID liked by the user's friends
    COUNT(af.friend_id) AS friends_likes -- Number of friends who liked the page
FROM 
    all_friends AS af
LEFT JOIN 
    likes AS l1 ON af.friend_id = l1.user_id -- Join friends with their liked pages
LEFT JOIN 
    likes AS l2 ON af.user_id = l2.user_id AND l1.page_id = l2.page_id 
    -- Check if the user has liked the page their friends liked
WHERE 
    l2.page_id IS NULL -- Exclude pages liked by the user
GROUP BY 
    af.user_id, l1.page_id -- Group by user and page ID
ORDER BY 
    af.user_id, l1.page_id; -- Optional ordering for clarity
