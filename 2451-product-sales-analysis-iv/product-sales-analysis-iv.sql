WITH UserSpending AS (
    SELECT 
        s.user_id,
        s.product_id,
        SUM(s.quantity * p.price) AS total_spending,
        RANK() OVER (PARTITION BY s.user_id ORDER BY SUM(s.quantity * p.price) DESC) AS rank_by_spending
    FROM 
        Sales s
    JOIN 
        Product p ON s.product_id = p.product_id
    GROUP BY 
        s.user_id, s.product_id
)
SELECT 
    user_id,
    product_id
FROM 
    UserSpending
WHERE 
    rank_by_spending = 1;
