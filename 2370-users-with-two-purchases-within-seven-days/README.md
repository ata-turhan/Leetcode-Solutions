<h2><a href="https://leetcode.com/problems/users-with-two-purchases-within-seven-days">Users With Two Purchases Within Seven Days</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>Purchases</code></p>

<pre>
+---------------+------+
| Column Name   | Type |
+---------------+------+
| purchase_id   | int  |
| user_id       | int  |
| purchase_date | date |
+---------------+------+
purchase_id contains unique values.
This table contains logs of the dates that users purchased from a certain retailer.
</pre>

<p>&nbsp;</p>

<p>Write a solution to report the IDs of the users that made any two purchases <strong>at most</strong> <code>7</code> days apart.</p>

<p>Return the result table ordered by <code>user_id</code>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Purchases table:
+-------------+---------+---------------+
| purchase_id | user_id | purchase_date |
+-------------+---------+---------------+
| 4           | 2       | 2022-03-13    |
| 1           | 5       | 2022-02-11    |
| 3           | 7       | 2022-06-19    |
| 6           | 2       | 2022-03-20    |
| 5           | 7       | 2022-06-19    |
| 2           | 2       | 2022-06-08    |
+-------------+---------+---------------+
<strong>Output:</strong> 
+---------+
| user_id |
+---------+
| 2       |
| 7       |
+---------+
<strong>Explanation:</strong> 
User 2 had two purchases on 2022-03-13 and 2022-03-20. Since the second purchase is within 7 days of the first purchase, we add their ID.
User 5 had only 1 purchase.
User 7 had two purchases on the same day so we add their ID.
</pre>
