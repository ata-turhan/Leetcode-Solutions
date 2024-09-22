# Query to rearrange the products table by converting the wide format (with multiple store columns) into a long format
# Each product_id is associated with store and price columns

# Select product_id, store name as 'store1', and its price where price is not NULL
SELECT product_id, 'store1' AS store, store1 AS price 
FROM products 
WHERE store1 IS NOT NULL

UNION

# Select product_id, store name as 'store2', and its price where price is not NULL
SELECT product_id, 'store2' AS store, store2 AS price 
FROM products 
WHERE store2 IS NOT NULL

UNION

# Select product_id, store name as 'store3', and its price where price is not NULL
SELECT product_id, 'store3' AS store, store3 AS price 
FROM products 
WHERE store3 IS NOT NULL;
