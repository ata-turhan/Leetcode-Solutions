<h2><a href="https://leetcode.com/problems/find-overlapping-shifts-ii">Find Overlapping Shifts II</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><p>Table: <code>EmployeeShifts</code></p>

<pre>
+------------------+----------+
| Column Name      | Type     |
+------------------+----------+
| employee_id      | int      |
| start_time       | datetime |
| end_time         | datetime |
+------------------+----------+
(employee_id, start_time) is the unique key for this table.
This table contains information about the shifts worked by employees, including the start time, and end time.
</pre>

<p>Write a solution to analyze overlapping shifts for each employee. Two shifts are considered overlapping if they occur on the <strong>same date</strong> and one shift&#39;s <code>end_time</code> is <strong>later than</strong> another shift&#39;s <code>start_time</code>.</p>

<p>For <strong>each employee</strong>, calculate the following:</p>

<ol>
	<li>The <strong>maximum</strong> number of shifts that <strong>overlap</strong> at any <strong>given time</strong>.</li>
	<li>The <strong>total duration</strong> of all overlaps in minutes.</li>
</ol>

<p><em>Return the result table ordered by</em> <code>employee_id</code> <em>in <strong>ascending</strong> order</em>.</p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<p><code>EmployeeShifts</code> table:</p>

<pre class="example-io">
+-------------+---------------------+---------------------+
| employee_id | start_time          | end_time            |
+-------------+---------------------+---------------------+
| 1           | 2023-10-01 09:00:00 | 2023-10-01 17:00:00 |
| 1           | 2023-10-01 15:00:00 | 2023-10-01 23:00:00 |
| 1           | 2023-10-01 16:00:00 | 2023-10-02 00:00:00 |
| 2           | 2023-10-01 09:00:00 | 2023-10-01 17:00:00 |
| 2           | 2023-10-01 11:00:00 | 2023-10-01 19:00:00 |
| 3           | 2023-10-01 09:00:00 | 2023-10-01 17:00:00 |
+-------------+---------------------+---------------------+
</pre>

<p><strong>Output:</strong></p>

<pre class="example-io">
+-------------+---------------------------+------------------------+
| employee_id | max_overlapping_shifts    | total_overlap_duration |
+-------------+---------------------------+------------------------+
| 1           | 3                         | 600                    |
| 2           | 2                         | 360                    |
| 3           | 1                         | 0                      |
+-------------+---------------------------+------------------------+
</pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Employee 1 has 3 shifts:
	<ul>
		<li>2023-10-01 09:00:00 to 2023-10-01 17:00:00</li>
		<li>2023-10-01 15:00:00 to 2023-10-01 23:00:00</li>
		<li>2023-10-01 16:00:00 to 2023-10-02 00:00:00</li>
	</ul>
	The maximum number of overlapping shifts is 3 (from 16:00 to 17:00). The total overlap duration is: - 2 hours (15:00-17:00) between 1st and 2nd shifts - 1 hour (16:00-17:00) between 1st and 3rd shifts - 7 hours (16:00-23:00) between 2nd and 3rd shifts Total: 10 hours = 600 minutes</li>
	<li>Employee 2 has 2 shifts:
	<ul>
		<li>2023-10-01 09:00:00 to 2023-10-01 17:00:00</li>
		<li>2023-10-01 11:00:00 to 2023-10-01 19:00:00</li>
	</ul>
	The maximum number of overlapping shifts is 2. The total overlap duration is 6 hours (11:00-17:00) = 360 minutes.</li>
	<li>Employee 3 has only 1 shift, so there are no overlaps.</li>
</ul>

<p>The output table contains the employee_id, the maximum number of simultaneous overlaps, and the total overlap duration in minutes for each employee, ordered by employee_id in ascending order.</p>
</div>
