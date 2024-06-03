-- CTE to calculate the number of distinct items sold by each seller and rank them
WITH ranks AS (
    SELECT 
        seller_id, 
        COUNT(DISTINCT item_id) AS num_items, 
        RANK() OVER (ORDER BY COUNT(DISTINCT item_id) DESC) AS rank_num 
    FROM 
        orders AS o 
    JOIN 
        items AS i USING(item_id) 
    JOIN 
        users AS u USING(seller_id) 
    WHERE 
        favorite_brand != item_brand 
    GROUP BY 
        seller_id
)

-- Main query to find the seller(s) with the highest number of distinct items sold
SELECT 
    seller_id, 
    num_items 
FROM 
    ranks 
WHERE 
    rank_num = 1;
