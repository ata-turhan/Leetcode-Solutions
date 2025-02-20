SELECT c.customer_id
FROM customer AS c
GROUP BY c.customer_id
HAVING COUNT(DISTINCT c.product_key) = (
    SELECT COUNT(DISTINCT p.product_key) FROM product AS p
);
