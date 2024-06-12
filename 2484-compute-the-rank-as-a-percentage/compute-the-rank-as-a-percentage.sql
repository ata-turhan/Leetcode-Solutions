with students_ranks as (
    select *, rank() over (partition by department_id order by mark desc) as rank_val, count(*) over (partition by department_id) as department_student_count from students
)
select student_id, department_id, ifnull(round((rank_val - 1) * 100 / (department_student_count - 1), 2), 0)  as percentage from students_ranks
