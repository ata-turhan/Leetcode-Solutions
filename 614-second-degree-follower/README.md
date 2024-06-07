<h2><a href="https://leetcode.com/problems/second-degree-follower">Second Degree Follower</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>Follow</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| followee    | varchar |
| follower    | varchar |
+-------------+---------+
(followee, follower) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates that the user follower follows the user followee on a social network.
There will not be a user following themself.
</pre>

<p>&nbsp;</p>

<p>A <strong>second-degree follower</strong> is a user who:</p>

<ul>
	<li>follows at least one user, and</li>
	<li>is followed by at least one user.</li>
</ul>

<p>Write a solution&nbsp;to report the <strong>second-degree users</strong> and the number of their followers.</p>

<p>Return the result table <strong>ordered</strong> by <code>follower</code> <strong>in alphabetical order</strong>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Follow table:
+----------+----------+
| followee | follower |
+----------+----------+
| Alice    | Bob      |
| Bob      | Cena     |
| Bob      | Donald   |
| Donald   | Edward   |
+----------+----------+
<strong>Output:</strong> 
+----------+-----+
| follower | num |
+----------+-----+
| Bob      | 2   |
| Donald   | 1   |
+----------+-----+
<strong>Explanation:</strong> 
User Bob has 2 followers. Bob is a second-degree follower because he follows Alice, so we include him in the result table.
User Donald has 1 follower. Donald is a second-degree follower because he follows Bob, so we include him in the result table.
User Alice has 1 follower. Alice is not a second-degree follower because she does not follow anyone, so we don not include her in the result table.
</pre>
