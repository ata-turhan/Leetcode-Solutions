-- MySQL query to select products that are both low fat and recyclable
SELECT 
    product_id 
FROM 
    products
WHERE 
    low_fats = 'Y' 
    AND recyclable = 'Y';
