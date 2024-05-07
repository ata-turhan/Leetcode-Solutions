# Write your MySQL query statement below
with cinema_with_rn as (
    select seat_id, row_number() over (partition by free order by seat_id asc) as rn from cinema where free = 1
),
consecutive_groups as (
    select min(seat_id) as first_seat_id, max(seat_id) as last_seat_id, count(*) as consecutive_seats_len  from cinema_with_rn group by seat_id - rn
)

select * from consecutive_groups where consecutive_seats_len = (select max(consecutive_seats_len) from consecutive_groups) order by first_seat_id asc