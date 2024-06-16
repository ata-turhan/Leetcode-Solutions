<h2><a href="https://leetcode.com/problems/find-all-unique-email-domains">Find All Unique Email Domains</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Table: <code>Emails</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
</pre>

<p>Write a solution to find all <strong>unique email domains</strong> and count the number of <strong>individuals</strong> associated with each domain. <strong>Consider only</strong> those domains that <strong>end</strong> with <strong>.com</strong>.</p>

<p>Return <em>the result table orderd by email domains in </em><strong>ascending</strong><em> order</em>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Emails table:
+-----+-----------------------+
| id  | email                 |
+-----+-----------------------+
| 336 | hwkiy@test.edu        |
| 489 | adcmaf@outlook.com    |
| 449 | vrzmwyum@yahoo.com    |
| 95  | tof@test.edu          |
| 320 | jxhbagkpm@example.org |
| 411 | zxcf@outlook.com      |
+----+------------------------+
<strong>Output:</strong> 
+--------------+-------+
| email_domain | count |
+--------------+-------+
| outlook.com  | 2     |
| yahoo.com    | 1     |  
+--------------+-------+
<strong>Explanation:</strong> 
- The valid domains ending with &quot;.com&quot; are only &quot;outlook.com&quot; and &quot;yahoo.com&quot;, with respective counts of 2 and 1.
Output table is ordered by email_domains in ascending order.
</pre>
