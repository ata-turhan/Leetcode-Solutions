-- CTE to recursively extract hashtags from tweets
WITH RECURSIVE ExtractTags AS (
    SELECT 
        SUBSTRING_INDEX(SUBSTRING_INDEX(tweet, "#", -1), " ", 1) AS tag,
        SUBSTRING(tweet, 1, LENGTH(tweet) - LOCATE('#', REVERSE(tweet))) AS remain
    FROM 
        Tweets
    WHERE 
        LOCATE('#', tweet) > 0
    UNION ALL
    SELECT 
        SUBSTRING_INDEX(SUBSTRING_INDEX(remain, "#", -1), " ", 1) AS tag,
        SUBSTRING(remain, 1, LENGTH(remain) - LOCATE('#', REVERSE(remain))) AS remain
    FROM 
        ExtractTags 
    WHERE 
        LOCATE('#', remain) > 0
),

-- CTE to count occurrences of each hashtag
CountedHashtags AS (
    SELECT 
        CONCAT("#", tag) AS hashtag, 
        COUNT(*) AS count  
    FROM 
        ExtractTags 
    GROUP BY 
        hashtag
)

-- Main query to select the top 3 hashtags by count, ordered alphabetically if counts are equal
SELECT 
    hashtag, 
    count 
FROM 
    CountedHashtags 
ORDER BY 
    count DESC, 
    hashtag DESC 
LIMIT 3;
