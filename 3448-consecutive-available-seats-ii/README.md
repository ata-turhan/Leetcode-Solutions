<h2><a href="https://leetcode.com/problems/consecutive-available-seats-ii">Consecutive Available Seats II</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>Cinema</code></p>

<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| seat_id     | int  |
| free        | bool |
+-------------+------+
seat_id is an auto-increment column for this table.
Each row of this table indicates whether the i<sup>th</sup> seat is free or not. 1 means free while 0 means occupied.
</pre>

<p>Write a solution to find the <strong>length</strong> of&nbsp;<strong>longest consecutive sequence</strong> of <strong>available</strong> seats in the cinema.</p>

<p>Note:</p>

<ul>
	<li>There will always be <strong>at most</strong> <strong>one</strong> longest consecutive sequence.</li>
	<li>If there are <strong>multiple</strong>&nbsp;consecutive sequences with the <strong>same length</strong>, include all of them in the output.</li>
</ul>

<p>Return <em>the result table <strong>ordered</strong> by</em> <code>first_seat_id</code> <em><strong>in ascending order</strong></em>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong>Example:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<p>Cinema table:</p>

<pre class="example-io">
+---------+------+
| seat_id | free |
+---------+------+
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
+---------+------+
</pre>

<p><strong>Output:</strong></p>

<pre class="example-io">
+-----------------+----------------+-----------------------+
| first_seat_id   | last_seat_id   | consecutive_seats_len |
+-----------------+----------------+-----------------------+
| 3               | 5              | 3                     |
+-----------------+----------------+-----------------------+
</pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Longest consecutive sequence of available seats starts from seat 3 and ends at seat 5 with a length of 3.</li>
</ul>
Output table is ordered by first_seat_id in ascending order.</div>
