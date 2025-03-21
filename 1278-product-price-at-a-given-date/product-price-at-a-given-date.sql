-- Return products that have no price history on or before 2019-08-16 (default price = 10)
SELECT DISTINCT 
    product_id, 
    10 AS price
FROM Products
WHERE product_id NOT IN (
    SELECT DISTINCT product_id 
    FROM Products 
    WHERE change_date <= '2019-08-16'
)

UNION

-- Return the latest price on or before 2019-08-16 for each product
SELECT 
    p.product_id, 
    p.new_price AS price
FROM Products p
JOIN (
    SELECT 
        product_id, 
        MAX(change_date) AS latest_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
) latest
ON p.product_id = latest.product_id AND p.change_date = latest.latest_date;
