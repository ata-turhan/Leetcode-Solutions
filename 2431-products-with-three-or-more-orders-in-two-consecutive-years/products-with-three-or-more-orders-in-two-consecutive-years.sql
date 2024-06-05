-- Step 1: Calculate the number of orders per product per year
WITH year_orders AS (
    SELECT 
        product_id, 
        YEAR(purchase_date) AS purchase_year, 
        COUNT(order_id) AS order_count
    FROM 
        orders
    GROUP BY 
        product_id, YEAR(purchase_date)
),
-- Step 2: Join the year_orders with itself to find consecutive years
consecutive_year_orders AS (
    SELECT 
        yo1.product_id,
        yo1.purchase_year AS year1,
        yo2.purchase_year AS year2,
        yo1.order_count AS count1,
        yo2.order_count AS count2
    FROM 
        year_orders yo1
    JOIN 
        year_orders yo2 
    ON 
        yo1.product_id = yo2.product_id
        AND yo2.purchase_year = yo1.purchase_year + 1
)
-- Step 3: Filter products that have 3 or more orders in two consecutive years
SELECT 
    DISTINCT product_id
FROM 
    consecutive_year_orders
WHERE 
    count1 >= 3 
    AND count2 >= 3;
