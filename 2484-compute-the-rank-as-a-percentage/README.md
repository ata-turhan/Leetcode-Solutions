<h2><a href="https://leetcode.com/problems/compute-the-rank-as-a-percentage">Compute the Rank as a Percentage</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>Students</code></p>

<pre>
+---------------+------+
| Column Name   | Type |
+---------------+------+
| student_id    | int  |
| department_id | int  |
| mark          | int  |
+---------------+------+
student_id contains unique values.
Each row of this table indicates a student&#39;s ID, the ID of the department in which the student enrolled, and their mark in the exam.
</pre>

<p>&nbsp;</p>

<p>Write a solution to report&nbsp;the rank of each student in their department as a percentage, where the rank as a percentage is computed using the following formula: <code>(student_rank_in_the_department - 1) * 100 / (the_number_of_students_in_the_department - 1)</code>. The <code>percentage</code> should be <strong>rounded to 2 decimal places</strong>. <code>student_rank_in_the_department</code> is determined by <strong>descending</strong><b> </b><code>mark</code>, such that the student with the highest <code>mark</code> is <code>rank 1</code>. If two students get the same mark, they also get the same rank.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The&nbsp;result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Students table:
+------------+---------------+------+
| student_id | department_id | mark |
+------------+---------------+------+
| 2          | 2             | 650  |
| 8          | 2             | 650  |
| 7          | 1             | 920  |
| 1          | 1             | 610  |
| 3          | 1             | 530  |
+------------+---------------+------+
<strong>Output:</strong> 
+------------+---------------+------------+
| student_id | department_id | percentage |
+------------+---------------+------------+
| 7          | 1             | 0.0        |
| 1          | 1             | 50.0       |
| 3          | 1             | 100.0      |
| 2          | 2             | 0.0        |
| 8          | 2             | 0.0        |
+------------+---------------+------------+
<strong>Explanation:</strong> 
For Department 1:
 - Student 7: percentage = (1 - 1) * 100 / (3 - 1) = 0.0
 - Student 1: percentage = (2 - 1) * 100 / (3 - 1) = 50.0
 - Student 3: percentage = (3 - 1) * 100 / (3 - 1) = 100.0
For Department 2:
 - Student 2: percentage = (1 - 1) * 100 / (2 - 1) = 0.0
 - Student 8: percentage = (1 - 1) * 100 / (2 - 1) = 0.0
</pre>
