with users_dates as (
    select user_id, created_at, row_number() over (partition by user_id order by created_at asc) as rn from users
),
users_dates_next_dates as (
    select us1.user_id, us1.created_at as prev_date, us2.created_at as next_date from users_dates as us1 join users_dates as us2 on us1.user_id = us2.user_id and us1.rn + 1 = us2.rn
)

select distinct user_id from users_dates_next_dates where datediff(next_date, prev_date) <= 7;
