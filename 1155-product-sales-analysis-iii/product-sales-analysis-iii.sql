SELECT 
    s1.product_id, 
    s1.year AS first_year, 
    s1.quantity, 
    s1.price
FROM sales AS s1
JOIN (
    SELECT 
        product_id, 
        MIN(year) AS year
    FROM sales
    GROUP BY product_id
) AS s2 
ON s1.product_id = s2.product_id AND s1.year = s2.year;
