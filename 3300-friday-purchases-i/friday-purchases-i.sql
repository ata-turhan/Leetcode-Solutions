# Write your MySQL query statement below
SELECT
	(WEEK(purchase_date) - WEEK('2023-11-01') + 1) AS 'week_of_month',
	purchase_date,
	SUM(amount_spend) AS 'total_amount'
FROM
	Purchases
WHERE
	DAYOFWEEK(purchase_date) = 6 # Friday
GROUP BY
	purchase_date
ORDER BY
	week_of_month