<h2><a href="https://leetcode.com/problems/second-day-verification">Second Day Verification</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Table: <code>emails</code></p>

<pre>
+-------------+----------+
| Column Name | Type     | 
+-------------+----------+
| email_id    | int      |
| user_id     | int      |
| signup_date | datetime |
+-------------+----------+
(email_id, user_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the email ID, user ID, and signup date.
</pre>

<p>Table: <code>texts</code></p>

<pre>
+---------------+----------+
| Column Name   | Type     | 
+---------------+----------+
| text_id       | int      |
| email_id      | int      |
| signup_action | enum     |
| action_date   | datetime |
+---------------+----------+
(text_id, email_id) is the primary key (combination of columns with unique values) for this table. 
signup_action is an enum type of (&#39;Verified&#39;, &#39;Not Verified&#39;). 
Each row of this table contains the text ID, email ID, signup action, and action date.
</pre>

<p>Write a Solution to find the user IDs of those who <strong>verified</strong> their <strong>sign-up</strong> on the <strong>second day</strong>.</p>

<p>Return <em>the result table ordered by</em> <code>user_id</code> <em>in <strong>ascending</strong> order</em>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<p>emails table:</p>

<pre class="example-io">
+----------+---------+---------------------+
| email_id | user_id | signup_date         |
+----------+---------+---------------------+
| 125      | 7771    | 2022-06-14 09:30:00|
| 433      | 1052    | 2022-07-09 08:15:00|
| 234      | 7005    | 2022-08-20 10:00:00|
+----------+---------+---------------------+
</pre>

<p>texts table:</p>

<pre class="example-io">
+---------+----------+--------------+---------------------+
| text_id | email_id | signup_action| action_date         |
+---------+----------+--------------+---------------------+
| 1       | 125      | Verified     | 2022-06-15 08:30:00|
| 2       | 433      | Not Verified | 2022-07-10 10:45:00|
| 4       | 234      | Verified     | 2022-08-21 09:30:00|
+---------+----------+--------------+---------------------+
    </pre>

<p><strong>Output:</strong></p>

<pre class="example-io">
+---------+
| user_id |
+---------+
| 7005    |
| 7771    |
+---------+
</pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li>User with email_id 7005 signed up on 2022-08-20 10:00:00 and&nbsp;verified on second day of the signup.</li>
	<li>User with email_id 7771 signed up on 2022-06-14 09:30:00 and&nbsp;verified on second day of the signup.</li>
</ul>
</div>
