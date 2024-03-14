SELECT 
    IF(minute % 6 = 0, minute DIV 6, minute DIV 6 + 1) AS interval_no, 
    SUM(order_count) AS total_orders 
FROM 
    orders 
GROUP BY 
   interval_no
ORDER BY 
    interval_no;
