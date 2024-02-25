# Write your MySQL query statement below
SELECT
    WEEK(purchase_date, 3) - WEEK('2023-11-01', 3) + 1 AS week_of_month,
    purchase_date,
    SUM(amount_spend) AS total_amount
FROM
    Purchases
WHERE
    DAYOFWEEK(purchase_date) = 6
GROUP BY
    week_of_month
ORDER BY
    week_of_month;
