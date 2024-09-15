SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15
ORDER BY tweet_id;
