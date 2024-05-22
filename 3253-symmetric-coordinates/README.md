<h2><a href="https://leetcode.com/problems/symmetric-coordinates">Symmetric Coordinates</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <font face="monospace"><code>Coordinates</code></font></p>

<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| X           | int  |
| Y           | int  |
+-------------+------+
Each row includes X and Y, where both are integers. Table may contain duplicate values.
</pre>

<p>Two coordindates <code>(X1, Y1)</code> and <code>(X2, Y2)</code> are said to be <strong>symmetric</strong> coordintes if <code>X1 == Y2</code> and <code>X2 == Y1</code>.</p>

<p>Write a solution that outputs, among all these <strong>symmetric</strong> <strong>coordintes</strong>, only those <strong>unique</strong> coordinates that satisfy the condition <code>X1 &lt;= Y1</code>.</p>

<p>Return <em>the result table ordered by </em><code>X</code> <em>and </em> <code>Y</code> <em>(respectively)</em> <em>in <strong>ascending order</strong></em>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Coordinates table:
+----+----+
| X  | Y  |
+----+----+
| 20 | 20 |
| 20 | 20 |
| 20 | 21 |
| 23 | 22 |
| 22 | 23 |
| 21 | 20 |
+----+----+
<strong>Output:</strong> 
+----+----+
| x  | y  |
+----+----+
| 20 | 20 |
| 20 | 21 |
| 22 | 23 |
+----+----+
<strong>Explanation:</strong> 
- (20, 20) and (20, 20) are symmetric coordinates because, X1 == Y2 and X2 == Y1. This results in displaying (20, 20) as a distinctive coordinates.
- (20, 21) and (21, 20) are symmetric coordinates because, X1 == Y2 and X2 == Y1. However, only (20, 21) will be displayed because X1 &lt;= Y1.
- (23, 22) and (22, 23) are symmetric coordinates because, X1 == Y2 and X2 == Y1. However, only (22, 23) will be displayed because X1 &lt;= Y1.
The output table is sorted by X and Y in ascending order.
</pre>
