-- Retrieve the number of students in each department, including departments with no students
SELECT 
    d.dept_name, -- Select the department name
    COUNT(s.student_id) AS student_number -- Count the number of students in each department
FROM 
    department d -- Alias for the department table
LEFT JOIN 
    student s USING (dept_id) -- Left join with the student table based on department ID
GROUP BY 
    d.dept_name -- Group by department name
ORDER BY 
    student_number DESC, -- Order by student number in descending order
    d.dept_name ASC; -- Then order by department name in ascending order
