<h2><a href="https://leetcode.com/problems/shortest-distance-in-a-plane">Shortest Distance in a Plane</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>Point2D</code></p>

<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
+-------------+------+
(x, y) is the primary key column (combination of columns with unique values) for this table.
Each row of this table indicates the position of a point on the X-Y plane.
</pre>

<p>&nbsp;</p>

<p>The distance between two points <code>p<sub>1</sub>(x<sub>1</sub>, y<sub>1</sub>)</code> and <code>p<sub>2</sub>(x<sub>2</sub>, y<sub>2</sub>)</code> is <code>sqrt((x<sub>2</sub> - x<sub>1</sub>)<sup>2</sup> + (y<sub>2</sub> - y<sub>1</sub>)<sup>2</sup>)</code>.</p>

<p>Write a solution to report the shortest distance between any two points from the <code>Point2D</code> table. Round the distance to <strong>two decimal points</strong>.</p>

<p>The&nbsp;result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Point2D table:
+----+----+
| x  | y  |
+----+----+
| -1 | -1 |
| 0  | 0  |
| -1 | -2 |
+----+----+
<strong>Output:</strong> 
+----------+
| shortest |
+----------+
| 1.00     |
+----------+
<strong>Explanation:</strong> The shortest distance is 1.00 from point (-1, -1) to (-1, 2).
</pre>
