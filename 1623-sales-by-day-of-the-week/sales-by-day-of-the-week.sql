WITH DayOfWeekSales AS (
    SELECT 
        i.item_category AS Category,
        DAYNAME(o.order_date) AS DayOfWeek,
        SUM(o.quantity) AS Quantity
    FROM 
        Orders o
    RIGHT JOIN 
        Items i ON o.item_id = i.item_id
    GROUP BY 
        i.item_category, DAYNAME(o.order_date)
)
SELECT 
    Category,
    COALESCE(SUM(CASE WHEN DayOfWeek = 'Monday' THEN Quantity ELSE 0 END), 0) AS Monday,
    COALESCE(SUM(CASE WHEN DayOfWeek = 'Tuesday' THEN Quantity ELSE 0 END), 0) AS Tuesday,
    COALESCE(SUM(CASE WHEN DayOfWeek = 'Wednesday' THEN Quantity ELSE 0 END), 0) AS Wednesday,
    COALESCE(SUM(CASE WHEN DayOfWeek = 'Thursday' THEN Quantity ELSE 0 END), 0) AS Thursday,
    COALESCE(SUM(CASE WHEN DayOfWeek = 'Friday' THEN Quantity ELSE 0 END), 0) AS Friday,
    COALESCE(SUM(CASE WHEN DayOfWeek = 'Saturday' THEN Quantity ELSE 0 END), 0) AS Saturday,
    COALESCE(SUM(CASE WHEN DayOfWeek = 'Sunday' THEN Quantity ELSE 0 END), 0) AS Sunday
FROM 
    DayOfWeekSales
GROUP BY 
    Category
ORDER BY 
    Category;
