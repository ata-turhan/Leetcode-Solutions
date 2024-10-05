WITH inactive_sellers AS (
    -- Select users who have fewer than 2 orders and classify them as inactive sellers
    SELECT 
        user_id, 
        'no' AS "2nd_item_fav_brand" 
    FROM 
        orders 
    RIGHT JOIN 
        users ON orders.seller_id = users.user_id 
    GROUP BY 
        user_id 
    HAVING 
        COUNT(order_id) < 2
),
active_sellers AS (
    -- Select orders of sellers who have at least 2 orders, excluding inactive sellers
    SELECT 
        * 
    FROM 
        orders 
    WHERE 
        seller_id NOT IN (SELECT user_id FROM inactive_sellers)
),
active_sellers_rank AS (
    -- Rank orders for active sellers to determine the second order (rank 2)
    SELECT 
        *, 
        ROW_NUMBER() OVER (PARTITION BY seller_id ORDER BY order_date ASC) AS ranks 
    FROM 
        active_sellers
)
-- Retrieve the second order of active sellers and check if it matches their favorite brand
SELECT 
    asr.seller_id, 
    IF(u.favorite_brand = i.item_brand, 'yes', 'no') AS "2nd_item_fav_brand" 
FROM 
    active_sellers_rank AS asr 
LEFT JOIN 
    users AS u ON asr.seller_id = u.user_id 
LEFT JOIN 
    items AS i ON asr.item_id = i.item_id 
WHERE 
    ranks = 2
-- Combine with the inactive sellers who have no second order
UNION ALL
SELECT 
    * 
FROM 
    inactive_sellers;
