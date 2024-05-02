# Write your MySQL query statement below
with ranks_tx as (
    select *, rank() over (partition by user_id order by transaction_date asc) as ranks from Transactions 
)
select r1.user_id, r1.spend as third_transaction_spend, r1.transaction_date as third_transaction_date   from ranks_tx as r1 left join ranks_tx as r2 on r1.ranks = 3 and r1.ranks - 1 = r2.ranks and r1.user_id = r2.user_id left join ranks_tx as r3 on r2.ranks - 1 = r3.ranks and  r1.user_id = r3.user_id where r1.spend > r2.spend and r1.spend > r3.spend