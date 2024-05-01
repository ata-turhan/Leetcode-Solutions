<h2><a href="https://leetcode.com/problems/find-longest-calls">Find Longest Calls</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>Contacts</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| first_name  | varchar |
| last_name   | varchar |
+-------------+---------+
id is the primary key (column with unique values) of this table.
id is a foreign key (reference column) to <code>Calls</code> table.
Each row of this table contains id, first_name, and last_name.
</pre>

<p>Table: <code>Calls</code></p>

<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| contact_id  | int  |
| type        | enum |
| duration    | int  |
+-------------+------+
(contact_id, type, duration) is the primary key (column with unique values) of this table.
type is an ENUM (category) type of (&#39;incoming&#39;, &#39;outgoing&#39;).
Each row of this table contains information about calls, comprising of contact_id, type, and duration in seconds.
</pre>

<p>Write a solution to find the <b>three longest&nbsp;</b><strong>incoming</strong> and <strong>outgoing</strong> calls.</p>

<p>Return t<em>he result table ordered by</em> <code>type</code>, <code>duration</code>, and<code> first_name</code>&nbsp;<em>in <strong>descending&nbsp;</strong>order and <code>duration</code> must be formatted as <strong>HH:MM:SS</strong>.</em></p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<p>Contacts table:</p>

<pre class="example-io">
+----+------------+-----------+
| id | first_name | last_name |
+----+------------+-----------+
| 1  | John       | Doe       |
| 2  | Jane       | Smith     |
| 3  | Alice      | Johnson   |
| 4  | Michael    | Brown     |
| 5  | Emily      | Davis     |
+----+------------+-----------+        
</pre>

<p>Calls table:</p>

<pre class="example-io">
+------------+----------+----------+
| contact_id | type     | duration |
+------------+----------+----------+
| 1          | incoming | 120      |
| 1          | outgoing | 180      |
| 2          | incoming | 300      |
| 2          | outgoing | 240      |
| 3          | incoming | 150      |
| 3          | outgoing | 360      |
| 4          | incoming | 420      |
| 4          | outgoing | 200      |
| 5          | incoming | 180      |
| 5          | outgoing | 280      |
+------------+----------+----------+
        </pre>

<p><strong>Output:</strong></p>

<pre class="example-io">
+-----------+----------+-------------------+
| first_name| type     | duration_formatted|
+-----------+----------+-------------------+
| Michael   | incoming | 00:07:00          |
| Jane      | incoming | 00:05:00          |
| Emily     | incoming | 00:03:00          |
| Alice     | outgoing | 00:06:00          |
| Emily     | outgoing | 00:04:40          |
| Jane      | outgoing | 00:04:00          |
+-----------+----------+-------------------+
        </pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Michael had an incoming call lasting 7 minutes.</li>
	<li>Jane had an incoming call lasting 5 minutes.</li>
	<li>Emily had an incoming call lasting 3 minutes.</li>
	<li>Alice had an outgoing call lasting 6 minutes.</li>
	<li>Emily had an outgoing call lasting 4 minutes and 40 seconds.</li>
	<li>Jane had an outgoing call lasting 4 minutes.</li>
</ul>

<p><b>Note:</b> Output table is sorted by type, duration, and first_name in descending order.</p>
</div>
