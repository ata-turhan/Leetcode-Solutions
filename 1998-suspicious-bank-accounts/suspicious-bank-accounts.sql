-- Step 1: Calculate the monthly income for each account by summing 'Creditor' transactions.
WITH MonthlyIncome AS (
    SELECT
        account_id,
        DATE_FORMAT(day, '%Y-%m') AS month,  -- Extract year-month from the transaction date
        SUM(amount) AS monthly_income        -- Sum the amount for each account and month
    FROM
        Transactions
    WHERE
        type = 'Creditor'                   -- Filter only 'Creditor' transactions (deposits)
    GROUP BY
        account_id, month                   -- Group by account and month
),

-- Step 2: Identify months where the monthly income exceeds the maximum allowed income for each account.
ExceededIncome AS (
    SELECT
        mi.account_id,
        mi.month,
        mi.monthly_income,
        a.max_income
    FROM
        MonthlyIncome mi
    JOIN
        Accounts a ON mi.account_id = a.account_id  -- Join with Accounts to get max_income
    WHERE
        mi.monthly_income > a.max_income            -- Filter months with income exceeding max_income
),

-- Step 3: Find accounts with two consecutive months where the income exceeded the maximum allowed.
ConsecutiveExceeded AS (
    SELECT
        e1.account_id
    FROM
        ExceededIncome e1
    JOIN
        ExceededIncome e2 ON e1.account_id = e2.account_id  -- Join with itself to find consecutive months
                         AND DATE_ADD(LAST_DAY(CONCAT(e1.month, '-01')), INTERVAL 1 DAY) = CONCAT(e2.month, '-01')
                         -- Ensure e1 and e2 are consecutive months
    GROUP BY
        e1.account_id  -- Group by account_id to get distinct accounts
)

-- Step 4: Select the IDs of suspicious accounts and order them.
SELECT
    account_id
FROM
    ConsecutiveExceeded
ORDER BY
    account_id;  -- Order the results by account_id
