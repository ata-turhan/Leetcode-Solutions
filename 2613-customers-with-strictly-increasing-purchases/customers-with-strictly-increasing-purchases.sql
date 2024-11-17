WITH RECURSIVE min_max_year AS (
    SELECT 
        MIN(YEAR(order_date)) AS min_year, 
        MAX(YEAR(order_date)) AS max_year
    FROM Orders
),
years AS (
    SELECT (SELECT min_year FROM min_max_year) AS year
    UNION ALL
    SELECT year + 1
    FROM years
    WHERE year + 1 <= (SELECT max_year FROM min_max_year)
),
customer_first_last_year AS (
    SELECT 
        customer_id, 
        MIN(YEAR(order_date)) AS first_year, 
        MAX(YEAR(order_date)) AS last_year
    FROM Orders
    GROUP BY customer_id
),
customer_years AS (
    SELECT 
        c.customer_id, 
        y.year
    FROM customer_first_last_year c
    JOIN years y ON y.year BETWEEN c.first_year AND c.last_year
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
