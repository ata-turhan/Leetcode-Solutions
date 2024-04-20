<h2><a href="https://leetcode.com/problems/friday-purchase-iii">Friday Purchase III </a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>Purchases</code></p>

<pre>
+---------------+------+
| Column Name   | Type |
+---------------+------+
| user_id       | int  |
| purchase_date | date |
| amount_spend  | int  |
+---------------+------+
(user_id, purchase_date, amount_spend) is the primary key (combination of columns with unique values) for this table.
purchase_date will range from November 1, 2023, to November 30, 2023, inclusive of both dates.
Each row contains user_id, purchase_date, and amount_spend.
</pre>

<p>Table: <code>Users</code></p>

<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| membership  | enum |
+-------------+------+
user_id is the primary key for this table.
membership is an ENUM (category) type of (&#39;Standard&#39;, &#39;Premium&#39;, &#39;VIP&#39;).
Each row of this table indicates the user_id, membership type.
</pre>

<p>Write a solution to calculate the <strong>total spending</strong> by <code>Premium</code>&nbsp;and <code>VIP</code> members on <strong>each Friday of every week</strong> in November 2023.&nbsp; If there are <strong>no purchases</strong> on a <strong>particular Friday</strong> by <code>Premium</code> or <code>VIP</code> members, it should be considered as <code>0</code>.</p>

<p>Return <em>the result table</em>&nbsp;<em>ordered by week of the month,&nbsp; and </em><code>membership</code><em> in <strong>ascending</strong> order</em>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<p>Purchases table:</p>

<pre class="example-io">
+---------+---------------+--------------+
| user_id | purchase_date | amount_spend |
+---------+---------------+--------------+
| 11      | 2023-11-03    | 1126         |
| 15      | 2023-11-10    | 7473         |
| 17      | 2023-11-17    | 2414         |
| 12      | 2023-11-24    | 9692         |
| 8       | 2023-11-24    | 5117         |
| 1       | 2023-11-24    | 5241         |
| 10      | 2023-11-22    | 8266         |
| 13      | 2023-11-21    | 12000        |
+---------+---------------+--------------+
</pre>

<p>Users table:</p>

<pre class="example-io">
+---------+------------+
| user_id | membership |
+---------+------------+
| 11      | Premium    |
| 15      | VIP        |
| 17      | Standard   |
| 12      | VIP        |
| 8       | Premium    |
| 1       | VIP        |
| 10      | Standard   |
| 13      | Premium    |
+---------+------------+
</pre>

<p><strong>Output:</strong></p>

<pre class="example-io">
+---------------+-------------+--------------+
| week_of_month | membership  | total_amount |
+---------------+-------------+--------------+
| 1             | Premium     | 1126         |
| 1             | VIP         | 0            |
| 2             | Premium     | 0            |
| 2             | VIP         | 7473         |
| 3             | Premium     | 0            |
| 3             | VIP         | 0            |
| 4             | Premium     | 5117         |
| 4             | VIP         | 14933        |
+---------------+-------------+--------------+
        </pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li>During the first week of November 2023, a transaction occurred on Friday, 2023-11-03, by a Premium member amounting to $1,126. No transactions were made by VIP members on this day, resulting in a value of 0.</li>
	<li>For the second week of November 2023, there was a transaction on Friday, 2023-11-10, and it was made by a VIP member, amounting to $7,473. Since there were no purchases by Premium members that Friday, the output shows 0 for Premium members.</li>
	<li>Similarly, during the third week of November 2023, no transactions by Premium or VIP members occurred on Friday, 2023-11-17, which shows 0 for both categories in this week.</li>
	<li>In the fourth week of November 2023, transactions occurred on Friday, 2023-11-24, involving one Premium member purchase of $5,117 and VIP member purchases totaling $14,933 ($9,692 from one and $5,241 from another).</li>
</ul>

<p><strong>Note:</strong> The output table is ordered by week_of_month and membership in ascending order.</p>
</div>
