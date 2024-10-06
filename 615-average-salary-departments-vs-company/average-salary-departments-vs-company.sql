with salary_employee as (
    select *,  date_format(pay_date, "%Y-%m") as pay_month from salary join employee using(employee_id)
),
company_salaries as (
    select avg(amount) as avg_comp, pay_month from salary_employee group by pay_month
),
department_salaries as (
    select avg(amount) as avg_dep, pay_month, department_id from salary_employee group by pay_month, department_id
)
select pay_month, department_id, 
(case 
when
avg_dep = avg_comp
then 
"same"
when
avg_dep > avg_comp
then 
"higher"
else
"lower"
end) as comparison

 from department_salaries join company_salaries using(pay_month)
