with gold_medals as (
    select user_id from users join contests on user_id = gold_medal group by user_id having count(contest_id) >= 3 
),
all_medals as (
    select user_id, contest_id as cur, lag(contest_id, 1) over (partition by user_id order by contest_id)  as prev, lead(contest_id, 1) over (partition by user_id order by contest_id) as next
    from users join contests on user_id = gold_medal or user_id = silver_medal  or user_id = bronze_medal
),
consecutive_medals as (
select distinct user_id from all_medals where cur = prev + 1 and cur = next - 1
)

select name, mail from users where user_id in (
    select user_id from gold_medals
    union
    select user_id from consecutive_medals
)



