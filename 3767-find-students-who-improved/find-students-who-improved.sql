WITH ranked_scores AS (
    SELECT 
        student_id, 
        subject, 
        score, 
        exam_date, 
        ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date ASC) AS ascending,
        ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS descending
    FROM scores
)

SELECT 
    r1.student_id, 
    r1.subject, 
    r1.score AS first_score, 
    r2.score AS latest_score
FROM ranked_scores AS r1
JOIN ranked_scores AS r2 
    ON r1.student_id = r2.student_id 
   AND r1.subject = r2.subject
WHERE 
    r1.ascending = 1 
    AND r2.descending = 1 
    AND r1.score < r2.score;
