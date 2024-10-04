-- Select the names of salespeople who did not sell to company 'RED'
SELECT
    s.name
FROM
    salesperson s
-- Use a subquery to find all sales_ids who sold to company 'RED'
WHERE
    s.sales_id NOT IN (
        SELECT
            o.sales_id
        FROM
            orders o
        LEFT JOIN
            company c ON o.com_id = c.com_id
        -- Only include records where the company name is 'RED'
        WHERE
            c.name = 'RED'
    );
