<h2><a href="https://leetcode.com/problems/find-the-missing-ids">Find the Missing IDs</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>Customers</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| customer_name | varchar |
+---------------+---------+
customer_id is the column with unique values for this table.
Each row of this table contains the name and the id customer.
</pre>

<p>&nbsp;</p>

<p>Write a solution to find the missing customer IDs. The missing IDs are ones that are not in the <code>Customers</code> table but are in the range between <code>1</code> and the <strong>maximum</strong> <code>customer_id</code> present in the table.</p>

<p><strong>Notice</strong> that the maximum <code>customer_id</code> will not exceed <code>100</code>.</p>

<p>Return the result table ordered by <code>ids</code> in <strong>ascending order</strong>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Customers table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Alice         |
| 4           | Bob           |
| 5           | Charlie       |
+-------------+---------------+
<strong>Output:</strong> 
+-----+
| ids |
+-----+
| 2   |
| 3   |
+-----+
<strong>Explanation:</strong> 
The maximum customer_id present in the table is 5, so in the range [1,5], IDs 2 and 3 are missing from the table.
</pre>
