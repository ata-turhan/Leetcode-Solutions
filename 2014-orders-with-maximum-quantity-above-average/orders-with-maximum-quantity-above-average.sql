WITH max_avg_quantity_per_order AS (
    SELECT order_id, MAX(quantity) AS max_quantity, AVG(quantity) AS avg_quantity 
    FROM ordersdetails 
    GROUP BY order_id
),
max_average_quantity AS (
    SELECT MAX(avg_quantity) AS max_avg_quantity 
    FROM max_avg_quantity_per_order
)

SELECT order_id 
FROM max_avg_quantity_per_order 
WHERE max_quantity > (SELECT max_avg_quantity FROM max_average_quantity);
