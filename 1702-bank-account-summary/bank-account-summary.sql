# Write your MySQL query statement below
with neg_bal as (
    select paid_by, -sum(amount) as bal from transactions group by paid_by
),
pos_bal as (
    select paid_to, sum(amount) as bal from transactions group by paid_to
)

select user_id, user_name, (credit + ifnull(n.bal, 0) + ifnull(p.bal, 0)) as credit, if((credit + ifnull(n.bal, 0) + ifnull(p.bal, 0)) < 0, "Yes", "No") as credit_limit_breached from   users as u left join neg_bal as n on u.user_id = n.paid_by left join pos_bal as p on u.user_id = p.paid_to