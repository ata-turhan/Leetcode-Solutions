-- CTE to calculate the total square footage and count of items for each item type
WITH category_footages AS (
    SELECT 
        item_type, 
        SUM(square_footage) AS total_footage, 
        COUNT(*) AS total_count 
    FROM 
        inventory 
    GROUP BY 
        item_type
)

-- Main query to calculate the item count based on the given conditions
SELECT 
    item_type,
    ( (500000 DIV total_footage) * total_count) AS item_count 
FROM 
    category_footages 
WHERE 
    item_type = 'prime_eligible'
UNION ALL
SELECT 
    item_type, 
    ( (500000 % (SELECT total_footage FROM category_footages WHERE item_type = 'prime_eligible') 
        DIV total_footage) * total_count) AS item_count 
FROM 
    category_footages 
WHERE 
    item_type = 'not_prime';
