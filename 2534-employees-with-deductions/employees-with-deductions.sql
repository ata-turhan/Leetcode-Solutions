with total_work_hours as (
    select employee_id, sum(TIME_TO_SEC(TIMEDIFF(out_time, in_time))/60 + if(TIME_TO_SEC(TIMEDIFF(out_time, in_time))%60 = 0, 0, 1))/60 as total_hours from logs group by employee_id
)
select employee_id from employees as e left join total_work_hours using(employee_id) where needed_hours > ifnull(total_hours, 0);
