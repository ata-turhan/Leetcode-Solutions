with ranked_employee as (
    select id, month, salary, rank() over (partition by id order by month desc) as ranks from employee
),
last_month_dropped_employee as (
    select id, month, salary from ranked_employee where ranks != 1
)
select l1.id, l1.month, (l1.salary + ifnull(l2.salary, 0) + ifnull(l3.salary, 0)) as Salary from last_month_dropped_employee as l1 left join last_month_dropped_employee as l2 on l1.id = l2.id and l1.month = l2.month + 1 left join last_month_dropped_employee as l3 on l1.id = l3.id and l1.month = l3.month + 2 order by id asc, month desc

