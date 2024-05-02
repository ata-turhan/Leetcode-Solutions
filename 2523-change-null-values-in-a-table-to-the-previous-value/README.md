<h2><a href="https://leetcode.com/problems/change-null-values-in-a-table-to-the-previous-value">Change Null Values in a Table to the Previous Value</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>CoffeeShop</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| drink       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row in this table shows the order id and the name of the drink ordered. Some drink rows are nulls.
</pre>

<p>&nbsp;</p>

<p>Write a solution to replace the <code>null</code> values of the drink with the name of the drink of the previous row that is not <code>null</code>. It is guaranteed that the drink on the first row of the table is not <code>null</code>.</p>

<p>Return the result table <strong>in the same order as the input</strong>.</p>

<p>The result format is shown in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
CoffeeShop table:
+----+-------------------+
| id | drink             |
+----+-------------------+
| 9  | Rum and Coke      |
| 6  | null              |
| 7  | null              |
| 3  | St Germain Spritz |
| 1  | Orange Margarita  |
| 2  | null              |
+----+-------------------+
<strong>Output:</strong> 
+----+-------------------+
| id | drink             |
+----+-------------------+
| 9  | Rum and Coke      |
| 6  | Rum and Coke      |
| 7  | Rum and Coke      |
| 3  | St Germain Spritz |
| 1  | Orange Margarita  |
| 2  | Orange Margarita  |
+----+-------------------+
<strong>Explanation:</strong> 
For ID 6, the previous value that is not null is from ID 9. We replace the null with &quot;Rum and Coke&quot;.
For ID 7, the previous value that is not null is from ID 9. We replace the null with &quot;Rum and Coke;.
For ID 2, the previous value that is not null is from ID 1. We replace the null with &quot;Orange Margarita&quot;.
Note that the rows in the output are the same as in the input.
</pre>
