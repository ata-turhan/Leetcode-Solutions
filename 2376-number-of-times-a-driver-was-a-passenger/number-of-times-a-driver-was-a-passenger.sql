# Write your MySQL query statement below
with unique_drivers as (
    select distinct(driver_id) as ddi from rides
)
select r1.ddi as driver_id, count(r2.passenger_id) as cnt from unique_drivers as r1 left join rides as r2 on r1.ddi = r2.passenger_id 
group by r1.ddi;