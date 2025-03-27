<h2><a href="https://leetcode.com/problems/find-students-who-improved">Find Students Who Improved</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>Scores</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student_id  | int     |
| subject     | varchar |
| score       | int     |
| exam_date   | varchar |
+-------------+---------+
(student_id, subject, exam_date) is the primary key for this table.
Each row contains information about a student&#39;s score in a specific subject on a particular exam date. score is between 0 and 100 (inclusive).
</pre>

<p>Write a solution to find the <strong>students who have shown improvement</strong>. A student is considered to have shown improvement if they meet <strong>both</strong> of these conditions:</p>

<ul>
	<li>Have taken exams in the <strong>same subject</strong> on at least two different dates</li>
	<li>Their <strong>latest score</strong> in that subject is <strong>higher</strong> than their <strong>first score</strong></li>
</ul>

<p>Return <em>the result table</em>&nbsp;<em>ordered by</em> <code>student_id,</code> <code>subject</code> <em>in <strong>ascending</strong> order</em>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<p>Scores table:</p>

<pre class="example-io">
+------------+----------+-------+------------+
| student_id | subject  | score | exam_date  |
+------------+----------+-------+------------+
| 101        | Math     | 70    | 2023-01-15 |
| 101        | Math     | 85    | 2023-02-15 |
| 101        | Physics  | 65    | 2023-01-15 |
| 101        | Physics  | 60    | 2023-02-15 |
| 102        | Math     | 80    | 2023-01-15 |
| 102        | Math     | 85    | 2023-02-15 |
| 103        | Math     | 90    | 2023-01-15 |
| 104        | Physics  | 75    | 2023-01-15 |
| 104        | Physics  | 85    | 2023-02-15 |
+------------+----------+-------+------------+
</pre>

<p><strong>Output:</strong></p>

<pre class="example-io">
+------------+----------+-------------+--------------+
| student_id | subject  | first_score | latest_score |
+------------+----------+-------------+--------------+
| 101        | Math     | 70          | 85           |
| 102        | Math     | 80          | 85           |
| 104        | Physics  | 75          | 85           |
+------------+----------+-------------+--------------+
</pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Student 101 in Math: Improved from 70 to 85</li>
	<li>Student 101 in Physics: No improvement (dropped from 65 to 60)</li>
	<li>Student 102 in Math: Improved from 80 to 85</li>
	<li>Student 103 in Math: Only one exam, not eligible</li>
	<li>Student 104 in Physics: Improved from 75 to 85</li>
</ul>

<p>Result table is ordered by student_id, subject.</p>
</div>
