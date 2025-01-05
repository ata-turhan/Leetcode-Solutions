SELECT 
    p.product_name, 
    SUM(o.unit) AS unit
FROM 
    products AS p
JOIN 
    orders AS o  
ON 
    p.product_id = o.product_id
WHERE 
    o.order_date LIKE '2020-02-%'
GROUP BY 
    p.product_name
HAVING 
    unit >= 100;
