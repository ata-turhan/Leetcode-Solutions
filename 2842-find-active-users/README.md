<h2><a href="https://leetcode.com/problems/find-active-users">Find Active Users</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table:<font face="monospace">&nbsp;<code>Users</code></font></p>

<pre>
+-------------+----------+ 
| Column Name | Type     | 
+-------------+----------+ 
| user_id     | int      | 
| item        | varchar  |
| created_at  | datetime |
| amount      | int      |
+-------------+----------+
This table may contain duplicate records. 
Each row includes the user ID, the purchased item, the date of purchase, and the purchase amount.
</pre>

<p>Write a solution to identify active users. An active user is a user that has made a second purchase <strong>within 7&nbsp;days&nbsp;</strong>of any other of their purchases.</p>

<p>For example, if the ending date is May 31, 2023.&nbsp;So any date between May 31, 2023, and June 7, 2023 (inclusive) would be considered &quot;within 7 days&quot; of May 31, 2023.</p>

<p>Return&nbsp;a list of&nbsp;<code>user_id</code>&nbsp;which denotes the list of active users&nbsp;in <strong>any order</strong>.</p>

<p>The&nbsp;result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:
</strong>Users table:
+---------+-------------------+------------+--------+ 
| user_id | item              | created_at | amount |  
+---------+-------------------+------------+--------+
| 5       | Smart Crock Pot   | 2021-09-18 | 698882 |
| 6       | Smart Lock        | 2021-09-14 | 11487  |
| 6       | Smart Thermostat  | 2021-09-10 | 674762 |
| 8       | Smart Light Strip | 2021-09-29 | 630773 |
| 4       | Smart Cat Feeder  | 2021-09-02 | 693545 |
| 4       | Smart Bed         | 2021-09-13 | 170249 |
+---------+-------------------+------------+--------+ 
<strong>Output:</strong>
+---------+
| user_id | 
+---------+
| 6       | 
+---------+
<strong>Explanation:</strong> 
- User with user_id 5 has only one transaction, so he is not an active user.
- User with user_id 6 has two transaction his first transaction was on 2021-09-10 and second transation was on 2021-09-14. The distance between the first and second transactions date is &lt;= 7 days. So he is an active user. 
- User with user_id 8 has only one transaction, so he is not an active user.  
- User with user_id 4 has two transaction his first transaction was on 2021-09-02 and second transation was on 2021-09-13. The distance between the first and second transactions date is &gt; 7 days. So he is not an active user. 
</pre>
