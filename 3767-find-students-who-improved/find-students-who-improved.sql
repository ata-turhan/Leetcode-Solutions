with ranks as (
    select student_id, subject, score, exam_date, 
    row_number() over ( partition by student_id, subject order by exam_date asc ) as ascending,
    row_number() over ( partition by student_id, subject order by exam_date desc ) as descending
    from scores
)
select r1. student_id, r2.subject, r1.score as first_score, r2.score as latest_score from ranks as r1 join ranks as r2 on r1.student_id = r2.student_id and  r1.subject = r2.subject
where r1.ascending = 1 and r2.descending = 1 and r1.score < r2.score