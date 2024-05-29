-- CTE to get the count and sum of approved transactions grouped by month and country
WITH ApprovedTransactions AS (
    SELECT
        DATE_FORMAT(trans_date, '%Y-%m') AS month,
        country,
        COUNT(*) AS approved_count,
        SUM(amount) AS approved_amount
    FROM
        Transactions
    WHERE
        state = 'approved'
    GROUP BY
        DATE_FORMAT(trans_date, '%Y-%m'), country
),
-- CTE to get the count and sum of chargeback transactions grouped by month and country
ChargebackTransactions AS (
    SELECT
        DATE_FORMAT(c.trans_date, '%Y-%m') AS month,
        t.country,
        COUNT(*) AS chargeback_count,
        SUM(t.amount) AS chargeback_amount
    FROM
        Chargebacks c
    JOIN
        Transactions t ON c.trans_id = t.id
    GROUP BY
        DATE_FORMAT(c.trans_date, '%Y-%m'), t.country
)
-- Main query to combine the results from both CTEs
SELECT
    at.month,
    at.country,
    at.approved_count,
    at.approved_amount,
    COALESCE(ct.chargeback_count, 0) AS chargeback_count,
    COALESCE(ct.chargeback_amount, 0) AS chargeback_amount
FROM
    ApprovedTransactions at
LEFT JOIN
    ChargebackTransactions ct ON at.month = ct.month AND at.country = ct.country

UNION

SELECT
    ct.month,
    ct.country,
    COALESCE(at.approved_count, 0) AS approved_count,
    COALESCE(at.approved_amount, 0) AS approved_amount,
    ct.chargeback_count,
    ct.chargeback_amount
FROM
    ChargebackTransactions ct
LEFT JOIN
    ApprovedTransactions at ON ct.month = at.month AND ct.country = at.country

-- Filter out rows where all counts and amounts are zero
WHERE
    (COALESCE(at.approved_count, 0) != 0 OR COALESCE(at.approved_amount, 0) != 0 OR 
    COALESCE(ct.chargeback_count, 0) != 0 OR COALESCE(ct.chargeback_amount, 0) != 0)
ORDER BY
    month, country;
