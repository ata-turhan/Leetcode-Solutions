<h2><a href="https://leetcode.com/problems/winning-candidate">Winning Candidate</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>Candidate</code></p>

<pre>
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
+-------------+----------+
id is the column with unique values for this table.
Each row of this table contains information about the id and the name of a candidate.
</pre>

<p>&nbsp;</p>

<p>Table: <code>Vote</code></p>

<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| candidateId | int  |
+-------------+------+
id is an auto-increment primary key (column with unique values).
candidateId is a foreign key (reference column) to id from the Candidate table.
Each row of this table determines the candidate who got the i<sup>th</sup> vote in the elections.
</pre>

<p>&nbsp;</p>

<p>Write a solution to report the name of the winning candidate (i.e., the candidate who got the largest number of votes).</p>

<p>The test cases are generated so that <strong>exactly one candidate wins</strong> the elections.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Candidate table:
+----+------+
| id | name |
+----+------+
| 1  | A    |
| 2  | B    |
| 3  | C    |
| 4  | D    |
| 5  | E    |
+----+------+
Vote table:
+----+-------------+
| id | candidateId |
+----+-------------+
| 1  | 2           |
| 2  | 4           |
| 3  | 3           |
| 4  | 2           |
| 5  | 5           |
+----+-------------+
<strong>Output:</strong> 
+------+
| name |
+------+
| B    |
+------+
<strong>Explanation:</strong> 
Candidate B has 2 votes. Candidates C, D, and E have 1 vote each.
The winner is candidate B.
</pre>
