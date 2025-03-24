SELECT ROUND(100 * AVG(
    CASE 
        WHEN temp.min_order_date = temp.min_delivery_date THEN 1 
        ELSE 0 
    END
), 2) AS immediate_percentage
FROM (
    SELECT 
        MIN(order_date) AS min_order_date, 
        MIN(customer_pref_delivery_date) AS min_delivery_date
    FROM delivery
    GROUP BY customer_id
) AS temp
