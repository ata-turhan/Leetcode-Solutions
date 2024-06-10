-- CTE to count the number of distinct courses for each major
WITH major_course_counts AS (
    SELECT 
        major, 
        COUNT(DISTINCT course_id) AS course_count 
    FROM 
        courses 
    GROUP BY 
        major
),

-- CTE to join students with their respective major course counts
student_course_counts AS (
    SELECT 
        s.*, 
        mcc.course_count 
    FROM 
        students AS s 
    JOIN 
        major_course_counts AS mcc 
    USING (major)
),

-- CTE to count the number of courses taken by each student and get their max grade
enrollment_course_count_max_grade AS (
    SELECT 
        e.student_id, 
        COUNT(DISTINCT e.course_id) AS taken_course_count, 
        MAX(e.grade) AS max_grade, 
        scc.course_count 
    FROM 
        enrollments AS e 
    JOIN 
        courses AS c 
    USING (course_id) 
    JOIN 
        student_course_counts AS scc 
    ON 
        c.major = scc.major 
        AND scc.student_id = e.student_id 
    GROUP BY 
        e.student_id
)

-- Main query to select students who have taken all courses in their major and have a max grade of 'A'
SELECT 
    student_id 
FROM 
    enrollment_course_count_max_grade 
WHERE 
    taken_course_count = course_count 
    AND max_grade = 'A';
