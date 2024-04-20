-- Generate weeks for Premium members
WITH RECURSIVE premium_weeks AS (
    SELECT 1 AS week_of_month, 'Premium' AS membership 
    UNION
    SELECT week_of_month + 1, 'Premium' AS membership FROM premium_weeks WHERE week_of_month < 4
),
-- Generate weeks for VIP members
vip_weeks AS (
    SELECT 1 AS week_of_month, 'VIP' AS membership 
    UNION
    SELECT week_of_month + 1, 'VIP' AS membership FROM vip_weeks WHERE week_of_month < 4
),
-- Combine weeks for Premium and VIP members
all_weeks AS (
    SELECT * FROM premium_weeks
    UNION
    SELECT * FROM vip_weeks
)
-- Main query to calculate total amount spent by Premium and VIP members for each week of the month
SELECT 
    a.week_of_month,
    a.membership, 
    IFNULL(SUM(p.amount_spend), 0) AS total_amount -- Sum of amount spent for each week and membership type
FROM 
    (SELECT * FROM purchases WHERE DAYOFWEEK(purchase_date) = 6) AS p -- Filter purchases for Fridays
JOIN 
    users AS u USING(user_id) -- Join with users table
RIGHT JOIN 
    all_weeks AS a ON FLOOR(DAY(p.purchase_date) / 7) + 1 = a.week_of_month AND u.membership = a.membership -- Join with all_weeks
GROUP BY 
    a.week_of_month, a.membership -- Group by week and membership
ORDER BY
    week_of_month, membership; -- Order the results
