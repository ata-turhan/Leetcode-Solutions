-- CTE to count the number of distinct courses for each major
WITH MajorCourseCounts AS (
    SELECT 
        major, 
        COUNT(DISTINCT course_id) AS course_count 
    FROM 
        courses 
    GROUP BY 
        major
),

-- CTE to join students with their respective major course counts
StudentMajorCourseCounts AS (
    SELECT 
        s.*, 
        mcc.course_count 
    FROM 
        students AS s 
    JOIN 
        MajorCourseCounts AS mcc 
    USING (major)
),

-- CTE to count the number of courses taken by each student and get their max grade
StudentEnrollmentStats AS (
    SELECT 
        e.student_id, 
        COUNT(DISTINCT e.course_id) AS taken_course_count, 
        MAX(e.grade) AS max_grade, 
        smcc.course_count 
    FROM 
        enrollments AS e 
    JOIN 
        courses AS c 
    USING (course_id) 
    JOIN 
        StudentMajorCourseCounts AS smcc 
    ON 
        c.major = smcc.major 
        AND smcc.student_id = e.student_id 
    GROUP BY 
        e.student_id
)

-- Main query to select students who have taken all courses in their major and have a max grade of 'A'
SELECT 
    student_id 
FROM 
    StudentEnrollmentStats 
WHERE 
    taken_course_count = course_count 
    AND max_grade = 'A';
