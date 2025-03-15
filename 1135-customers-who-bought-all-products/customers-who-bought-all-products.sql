WITH distinct_product_count AS (
    SELECT COUNT(DISTINCT product_key) AS total_products
    FROM product
)
SELECT c.customer_id
FROM customer c
JOIN distinct_product_count dpc 
GROUP BY c.customer_id
HAVING COUNT(DISTINCT c.product_key) = MAX(dpc.total_products);
