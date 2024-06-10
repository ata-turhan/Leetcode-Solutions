with major_course_counts as (
    select major, count(distinct course_id) as course_count from courses group by major
),
student_course_counts as (
    select * from students join major_course_counts using(major)
),
enrollment_course_count_max_grade as (
    select e.student_id, count(distinct course_id) as taken_course_count, max(grade) as max_grade, course_count from enrollments as e join courses as c using(course_id) join student_course_counts as s on c.major = s.major and s.student_id = e.student_id group by e.student_id
)

select student_id from enrollment_course_count_max_grade where taken_course_count = course_count and max_grade = "A"