WITH RECURSIVE YearRange AS (
    -- Generate a range of years spanning the min and max order dates
    SELECT 
        MIN(YEAR(order_date)) AS min_year, 
        MAX(YEAR(order_date)) AS max_year
    FROM Orders
),
Years AS (
    -- Create a sequential year list using recursion
    SELECT (SELECT min_year FROM YearRange) AS year
    UNION ALL
    SELECT year + 1
    FROM Years
    WHERE year + 1 <= (SELECT max_year FROM YearRange)
),
CustomerFirstLastYear AS (
    -- Determine the first and last active years for each customer
    SELECT 
        customer_id, 
        MIN(YEAR(order_date)) AS first_year, 
        MAX(YEAR(order_date)) AS last_year
    FROM Orders
    GROUP BY customer_id
),
CustomerYears AS (
    -- Assign all relevant years to each customer between their first and last order years
    SELECT 
        c.customer_id, 
        y.year
    FROM CustomerFirstLastYear c
    JOIN Years y ON y.year BETWEEN c.first_year AND c.last_year
),
CustomerYearPurchases AS (
    -- Calculate total purchases for each customer by year, filling gaps with 0
    SELECT 
        cy.customer_id, 
        cy.year,
        COALESCE(SUM(o.price), 0) AS total_purchase
    FROM CustomerYears cy
    LEFT JOIN Orders o 
        ON cy.customer_id = o.customer_id 
        AND YEAR(o.order_date) = cy.year
    GROUP BY cy.customer_id, cy.year
),
CustomerPurchasesWithLag AS (
    -- Add the previous year's total purchase as a lag column
    SELECT 
        cp.customer_id, 
        cp.year, 
        cp.total_purchase,
        LAG(cp.total_purchase) OVER (PARTITION BY cp.customer_id ORDER BY cp.year) AS prev_total_purchase
    FROM CustomerYearPurchases cp
),
CustomersWithNonIncreasingPurchases AS (
    -- Identify customers where the yearly purchase is not strictly increasing
    SELECT DISTINCT customer_id
    FROM CustomerPurchasesWithLag
    WHERE prev_total_purchase IS NOT NULL AND total_purchase <= prev_total_purchase
)
-- Select customers whose purchases are strictly increasing
SELECT customer_id
FROM CustomerFirstLastYear
WHERE customer_id NOT IN (SELECT customer_id FROM CustomersWithNonIncreasingPurchases);
