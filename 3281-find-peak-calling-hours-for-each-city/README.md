<h2><a href="https://leetcode.com/problems/find-peak-calling-hours-for-each-city">Find Peak Calling Hours for Each City</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>Calls</code></p>

<pre>
+--------------+----------+
| Column Name  | Type     |
+--------------+----------+
| caller_id    | int      |
| recipient_id | int      |
| call_time    | datetime |
| city         | varchar  |
+--------------+----------+
(caller_id, recipient_id, call_time) is the primary key (combination of columns with unique values) for this table.
Each row contains caller id, recipient id, call time, and city.
</pre>

<p>Write a solution to find the <strong>peak</strong> calling <strong>hour</strong> for each <code>city</code>. If <strong>multiple hours</strong> have the <strong>same</strong> number of calls, all of those hours will be recognized as <strong>peak hours </strong>for that specific city.</p>

<p>Return <em>the result table ordered by <strong>peak calling hour</strong> and </em><code>city</code><em> in <strong>descending</strong></em><em><strong> </strong>order.</em></p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Calls table:
+-----------+--------------+---------------------+----------+
| caller_id | recipient_id | call_time           | city     |
+-----------+--------------+---------------------+----------+
| 8         | 4            | 2021-08-24 22:46:07 | Houston  |
| 4         | 8            | 2021-08-24 22:57:13 | Houston  |  
| 5         | 1            | 2021-08-11 21:28:44 | Houston  |  
| 8         | 3            | 2021-08-17 22:04:15 | Houston  |
| 11        | 3            | 2021-08-17 13:07:00 | New York |
| 8         | 11           | 2021-08-17 14:22:22 | New York |
+-----------+--------------+---------------------+----------+
<strong>Output:</strong> 
+----------+-------------------+-----------------+
| city     | peak_calling_hour | number_of_calls |
+----------+-------------------+-----------------+
| Houston  | 22                | 3               |
| New York | 14                | 1               |
| New York | 13                | 1               |
+----------+-------------------+-----------------+
<strong>Explanation:</strong> 
For Houston:
  - The peak time is 22:00, with a total of 3 calls recorded. 
For New York:
  - Both 13:00 and 14:00 hours have equal call counts of 1, so both times are considered peak hours.
Output table is ordered by peak_calling_hour and city in descending order.</pre>
