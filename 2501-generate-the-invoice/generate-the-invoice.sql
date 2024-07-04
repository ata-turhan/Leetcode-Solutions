-- CTE to join purchases and products, forming product purchases
WITH ProductPurchases AS (
    SELECT 
        pu.invoice_id, 
        pu.product_id, 
        pu.quantity, 
        po.price 
    FROM 
        purchases AS pu 
    JOIN 
        products AS po USING (product_id)
),

-- CTE to calculate the total cost of each invoice and find the invoice with the highest total cost
OrderedInvoices AS (
    SELECT 
        invoice_id, 
        SUM(quantity * price) AS total_cost 
    FROM 
        ProductPurchases 
    GROUP BY 
        invoice_id 
    ORDER BY 
        total_cost DESC, invoice_id ASC 
    LIMIT 1
)

-- Main query to select product details for the invoice with the highest total cost
SELECT 
    product_id, 
    quantity, 
    (quantity * price) AS price 
FROM 
    ProductPurchases 
WHERE 
    invoice_id = (SELECT invoice_id FROM OrderedInvoices);
