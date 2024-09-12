-- Query to find customers who never placed an order
SELECT 
    name AS Customers 
FROM 
    Customers c
LEFT JOIN 
    Orders o ON c.id = o.customerId
WHERE 
    o.id IS NULL;  -- Ensure the customer has no matching orders
