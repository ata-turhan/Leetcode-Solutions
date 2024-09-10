with ordered_seniors as (
    select employee_id, salary, sum(salary) over (order by salary asc) as cum_sal from candidates where experience = "Senior"
),
hired_seniors as (
    select employee_id, salary from ordered_seniors where cum_sal <= 70000
),
total_hired_senior_salaries as (
    select ifnull(sum(salary), 0) as sum_sal from hired_seniors 
),
ordered_juniors as (
    select employee_id, sum(salary) over (order by salary asc) as cum_sal from candidates where experience = "Junior"
),
hired_juniors as (
    select employee_id from ordered_juniors where cum_sal + (select sum_sal from total_hired_senior_salaries) <= 70000
)
select employee_id from hired_seniors
union all
select employee_id from hired_juniors


