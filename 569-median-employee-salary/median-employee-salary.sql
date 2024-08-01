with ranked_employees as (
    select *, rank() over (partition by company order by salary asc, id asc) as ranks from employee
), 
odd_values as (
    select company, count(*) as total_count from ranked_employees group by company having count(*) % 2 = 1
),
even_values as (
    select company, count(*) as total_count from ranked_employees group by company having count(*) % 2 = 0
)
select id, company, salary from ranked_employees as re join even_values as ov using(company) where re.ranks in (total_count div 2, total_count div 2 + 1)
union all
select id, company, salary from ranked_employees as re join odd_values as ov using(company) where re.ranks = total_count div 2 + 1;
