WITH post_keywords AS (
    SELECT 
        p.post_id,
        k.topic_id
    FROM 
        Posts p
    JOIN 
        Keywords k ON CONCAT(' ', LOWER(p.content), ' ') LIKE CONCAT('% ', LOWER(k.word), ' %')
    GROUP BY 
        p.post_id, k.topic_id
),
post_topics AS (
    SELECT 
        post_id,
        GROUP_CONCAT(topic_id ORDER BY topic_id) AS topic
    FROM 
        post_keywords
    GROUP BY 
        post_id
),
all_posts AS (
    SELECT 
        p.post_id,
        COALESCE(pt.topic, 'Ambiguous!') AS topic
    FROM 
        Posts p
    LEFT JOIN 
        post_topics pt ON p.post_id = pt.post_id
)
SELECT * FROM all_posts
ORDER BY post_id;
