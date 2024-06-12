-- CTE to rank students within each department and count the number of students in each department
WITH students_ranks AS (
    SELECT 
        student_id,
        department_id,
        mark,
        RANK() OVER (PARTITION BY department_id ORDER BY mark DESC) AS rank_val,
        COUNT(*) OVER (PARTITION BY department_id) AS department_student_count
    FROM 
        students
)

-- Main query to calculate the percentile rank of each student within their department
SELECT 
    student_id, 
    department_id,
    -- Calculate the percentile rank
    IFNULL(
        ROUND((rank_val - 1) * 100 / (department_student_count - 1), 2), 
        0
    ) AS percentage
FROM 
    students_ranks;
