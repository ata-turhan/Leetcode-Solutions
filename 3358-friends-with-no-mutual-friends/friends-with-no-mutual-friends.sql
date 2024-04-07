-- This query selects pairs of users who are friends with each other and have no mutual friends.

-- Create a common table expression (CTE) to get all pairs of friends
WITH AllPairs AS (
    SELECT user_id1, user_id2 FROM Friends
    UNION ALL 
    SELECT user_id2, user_id1 FROM Friends
),
-- Create a common table expression (CTE) to find pairs of users who have mutual friends
SharedFriendPairs AS (
    SELECT A1.user_id1 AS user_id1,
        A2.user_id1 AS user_id2
    FROM AllPairs A1
    JOIN AllPairs A2 ON A1.user_id2 = A2.user_id2
)
-- Select pairs of users who are friends with each other and have no mutual friends
SELECT 
    f1.user_id1, -- Select the first user ID from the first friend pair
    f1.user_id2 -- Select the second user ID from the first friend pair
FROM 
    Friends f1 -- Alias for the first instance of the Friends table
WHERE 
    -- Filter out pairs where the combination of user_id1 and user_id2 is not found in the list of pairs with mutual friends
    (f1.user_id1, f1.user_id2) NOT IN (
        -- Subquery to find pairs of users who have mutual friends
        SELECT 
            user_id1, -- Select the user ID from the first subquery
            user_id2 -- Select the user ID from the second subquery
        FROM 
            SharedFriendPairs -- CTE to find pairs of users who have mutual friends
    )
ORDER BY 
    f1.user_id1, f1.user_id2; -- Order the result by user_id1 and user_id2 in ascending order
