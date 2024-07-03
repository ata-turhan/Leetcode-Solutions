with passenger_order as (
    select *, row_number() over ( partition by flight_id order by booking_time) as passenger_number from passengers as p join flights as f using(flight_id) 
)
select passenger_id, if(passenger_number <= capacity, "Confirmed", "Waitlist") as Status     from passenger_order order by passenger_id
