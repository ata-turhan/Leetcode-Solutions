with bus_orders as (
    select bus_id, arrival_time, row_number() over (order by arrival_time asc) as rn from buses
),
bus_intervals as (
    select b1.bus_id, b1.arrival_time, ifnull(b2.arrival_time, -1)  as prev_arrival_time from bus_orders as b1 left join bus_orders as b2 on b1.rn = b2.rn+1
)

select bus_id, count(passenger_id) as passengers_cnt  from bus_intervals left join passengers on bus_intervals.prev_arrival_time < passengers.arrival_time and passengers.arrival_time <= bus_intervals.arrival_time group by bus_id order by bus_id asc;
