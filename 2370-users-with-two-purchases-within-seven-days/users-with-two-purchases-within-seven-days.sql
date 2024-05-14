with ordered_purchases as (
    select user_id, purchase_date, row_number() over (partition by user_id order by purchase_date asc) as rn from purchases 
),
ordered_purchases_with_prev_purchase as (
    select op1.user_id, op1.purchase_date as next_date, op2.purchase_date as prev_date from ordered_purchases as op1 join ordered_purchases as op2 on op1.user_id = op2.user_id and op1.rn = op2.rn+1
)

select distinct user_id from ordered_purchases_with_prev_purchase where datediff(next_date, prev_date) <= 7 order by user_id;