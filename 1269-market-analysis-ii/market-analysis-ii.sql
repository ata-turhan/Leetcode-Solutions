WITH InactiveSellers AS (
    -- Select users with fewer than 2 orders and classify them as inactive sellers
    SELECT 
        u.user_id, 
        'no' AS "2nd_item_fav_brand"
    FROM 
        users u
    LEFT JOIN 
        orders o ON u.user_id = o.seller_id 
    GROUP BY 
        u.user_id 
    HAVING 
        COUNT(o.order_id) < 2
),
ActiveSellers AS (
    -- Select orders of sellers who have at least 2 orders, excluding inactive sellers
    SELECT 
        * 
    FROM 
        orders o
    WHERE 
        o.seller_id NOT IN (SELECT user_id FROM InactiveSellers)
),
RankedActiveSellers AS (
    -- Rank orders for active sellers to determine the second order (rank 2)
    SELECT 
        o.*, 
        ROW_NUMBER() OVER (PARTITION BY o.seller_id ORDER BY o.order_date ASC) AS order_rank 
    FROM 
        ActiveSellers o
)
-- Retrieve the second order of active sellers and check if it matches their favorite brand
SELECT 
    ras.seller_id, 
    IF(u.favorite_brand = i.item_brand, 'yes', 'no') AS "2nd_item_fav_brand"
FROM 
    RankedActiveSellers ras
LEFT JOIN 
    users u ON ras.seller_id = u.user_id 
LEFT JOIN 
    items i ON ras.item_id = i.item_id 
WHERE 
    ras.order_rank = 2
-- Combine with inactive sellers who do not have a second order
UNION ALL
SELECT 
    *
FROM 
    InactiveSellers isel;
