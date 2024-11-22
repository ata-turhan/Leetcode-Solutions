<h2><a href="https://leetcode.com/problems/find-median-given-frequency-of-numbers">Find Median Given Frequency of Numbers</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><p>Table: <code>Numbers</code></p>

<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
| frequency   | int  |
+-------------+------+
num is the primary key (column with unique values) for this table.
Each row of this table shows the frequency of a number in the database.
</pre>

<p>&nbsp;</p>

<p>The <a href="https://en.wikipedia.org/wiki/Median" target="_blank"><strong>median</strong></a> is the value separating the higher half from the lower half of a data sample.</p>

<p>Write a solution to report the <strong>median</strong> of all the numbers in the database after decompressing the <code>Numbers</code> table. Round the median to <strong>one decimal point</strong>.</p>

<p>The&nbsp;result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Numbers table:
+-----+-----------+
| num | frequency |
+-----+-----------+
| 0   | 7         |
| 1   | 1         |
| 2   | 3         |
| 3   | 1         |
+-----+-----------+
<strong>Output:</strong> 
+--------+
| median |
+--------+
| 0.0    |
+--------+
<strong>Explanation:</strong> 
If we decompress the Numbers table, we will get [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3], so the median is (0 + 0) / 2 = 0.
</pre>
