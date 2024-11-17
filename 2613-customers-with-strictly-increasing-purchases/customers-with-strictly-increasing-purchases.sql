WITH customer_first_last_year AS (
    SELECT 
        customer_id, 
        MIN(YEAR(order_date)) AS first_year, 
        MAX(YEAR(order_date)) AS last_year
    FROM Orders
    GROUP BY customer_id
),
numbers AS (
    SELECT 0 AS n UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 
    UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9
    UNION ALL SELECT 10 UNION ALL SELECT 11 UNION ALL SELECT 12 UNION ALL SELECT 13 UNION ALL SELECT 14
    UNION ALL SELECT 15 UNION ALL SELECT 16 UNION ALL SELECT 17 UNION ALL SELECT 18 UNION ALL SELECT 19
    UNION ALL SELECT 20  -- Extend this list if the range of years is larger
),
customer_years AS (
    SELECT 
        c.customer_id, 
        c.first_year + n.n AS year
    FROM customer_first_last_year c
    JOIN numbers n ON n.n <= c.last_year - c.first_year
),
customer_year_purchases AS (
    SELECT 
        cy.customer_id, 
        cy.year,
        COALESCE(SUM(o.price), 0) AS total_purchase
    FROM customer_years cy
    LEFT JOIN Orders o ON cy.customer_id = o.customer_id AND YEAR(o.order_date) = cy.year
    GROUP BY cy.customer_id, cy.year
),
customer_purchases_lag AS (
    SELECT 
        cp.customer_id, 
        cp.year, 
        cp.total_purchase,
        LAG(cp.total_purchase) OVER (PARTITION BY cp.customer_id ORDER BY cp.year) AS prev_total_purchase
    FROM customer_year_purchases cp
),
customers_with_non_increasing_purchases AS (
    SELECT DISTINCT customer_id
    FROM customer_purchases_lag
    WHERE prev_total_purchase IS NOT NULL AND total_purchase <= prev_total_purchase
)
SELECT customer_id
FROM customer_first_last_year
WHERE customer_id NOT IN (SELECT customer_id FROM customers_with_non_increasing_purchases);
