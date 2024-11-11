WITH RECURSIVE
    -- Generate numbers from 0 up to the maximum transactions_count
    Numbers AS (
        SELECT 0 AS transactions_count
        UNION ALL
        SELECT transactions_count + 1
        FROM Numbers
        WHERE transactions_count + 1 <= (
            SELECT MAX(transactions_count)
            FROM (
                SELECT
                    v.user_id,
                    v.visit_date,
                    COUNT(t.transaction_date) AS transactions_count
                FROM
                    Visits v
                LEFT JOIN
                    Transactions t
                ON
                    v.user_id = t.user_id AND v.visit_date = t.transaction_date
                GROUP BY
                    v.user_id,
                    v.visit_date
            ) AS TransactionsPerVisit
        )
    ),
    -- Calculate transactions per visit
    TransactionsPerVisit AS (
        SELECT
            v.user_id,
            v.visit_date,
            COUNT(t.transaction_date) AS transactions_count
        FROM
            Visits v
        LEFT JOIN
            Transactions t
        ON
            v.user_id = t.user_id AND v.visit_date = t.transaction_date
        GROUP BY
            v.user_id,
            v.visit_date
    ),
    -- Aggregate visits by transactions_count
    VisitCounts AS (
        SELECT
            transactions_count,
            COUNT(*) AS visits_count
        FROM
            TransactionsPerVisit
        GROUP BY
            transactions_count
    )
SELECT
    n.transactions_count,
    COALESCE(vc.visits_count, 0) AS visits_count
FROM
    Numbers n
LEFT JOIN
    VisitCounts vc
ON
    n.transactions_count = vc.transactions_count
ORDER BY
    n.transactions_count;
