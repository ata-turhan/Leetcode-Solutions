-- Main query to find invalid tweets based on the given criteria
SELECT 
    tweet_id
FROM 
    Tweets
WHERE 
    -- Condition to check if the tweet exceeds 140 characters in length
    LENGTH(content) > 140 
    OR 
    -- Condition to check if the tweet has more than 3 mentions
    (LENGTH(content) - LENGTH(REPLACE(content, '@', ''))) > 3
    OR 
    -- Condition to check if the tweet has more than 3 hashtags
    (LENGTH(content) - LENGTH(REPLACE(content, '#', ''))) > 3
ORDER BY 
    tweet_id ASC;
