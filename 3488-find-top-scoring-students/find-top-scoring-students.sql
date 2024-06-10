-- CTE to count the number of distinct courses for each major
WITH MajorCourseCounts AS (
    SELECT 
        major, 
        COUNT(DISTINCT course_id) AS total_courses 
    FROM 
        courses 
    GROUP BY 
        major
),

-- CTE to join students with their respective major course counts
StudentMajorCourseCounts AS (
    SELECT 
        s.student_id, 
        s.major, 
        mcc.total_courses 
    FROM 
        students AS s 
    JOIN 
        MajorCourseCounts AS mcc 
    USING (major)
),

-- CTE to count the number of courses taken by each student and get their lowest grade
StudentEnrollmentStats AS (
    SELECT 
        e.student_id, 
        COUNT(DISTINCT e.course_id) AS taken_courses, 
        MAX(e.grade) AS lowest_grade, 
        smcc.total_courses 
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
    taken_courses = total_courses 
    AND lowest_grade = 'A';
