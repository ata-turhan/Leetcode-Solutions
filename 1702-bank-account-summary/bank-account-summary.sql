-- Common Table Expression to calculate negative balances for users who paid
WITH neg_bal AS (
    SELECT paid_by, -SUM(amount) AS bal FROM transactions GROUP BY paid_by
),
-- Common Table Expression to calculate positive balances for users who received payments
pos_bal AS (
    SELECT paid_to, SUM(amount) AS bal FROM transactions GROUP BY paid_to
)
-- Main query to retrieve user information along with their credit balances and whether their credit limit is breached
SELECT 
    u.user_id, -- User ID
    u.user_name, -- User Name
    (u.credit + IFNULL(n.bal, 0) + IFNULL(p.bal, 0)) AS credit, -- Total credit balance
    IF((u.credit + IFNULL(n.bal, 0) + IFNULL(p.bal, 0)) < 0, "Yes", "No") AS credit_limit_breached -- Whether credit limit is breached
FROM   
    users AS u -- Users table
LEFT JOIN 
    neg_bal AS n ON u.user_id = n.paid_by -- Joining with negative balances
LEFT JOIN 
    pos_bal AS p ON u.user_id = p.paid_to -- Joining with positive balances
