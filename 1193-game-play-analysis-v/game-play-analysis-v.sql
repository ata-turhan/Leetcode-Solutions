with activity_with_ranks_and_next_dates as (
    select event_date, rank() over (partition by player_id order by event_date asc) as day_rank, lead(event_date, 1) over (partition by player_id order by event_date asc) as next_date from activity
),
dates_and_retention as (
    select event_date, datediff(next_date, event_date) = 1 as has_retention from activity_with_ranks_and_next_dates where day_rank = 1
)
select event_date as install_dt, count(event_date) as installs, round(sum(ifnull(has_retention, 0)) / count(event_date), 2) as Day1_retention  from dates_and_retention group by event_date