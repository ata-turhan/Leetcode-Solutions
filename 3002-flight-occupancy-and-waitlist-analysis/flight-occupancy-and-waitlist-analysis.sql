with customer_orders as (
    select *, row_number() over (partition by flight_id order by passenger_id asc) as rn from flights as f left join passengers as p using(flight_id)
)

select flight_id, sum(if(passenger_id is null, 0, if(rn <= capacity, 1, 0))) as booked_cnt, sum(if(passenger_id is null, 0, if(rn > capacity, 1, 0))) as waitlist_cnt from customer_orders group by flight_id order by flight_id asc;
