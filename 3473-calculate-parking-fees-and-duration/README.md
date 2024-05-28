<h2><a href="https://leetcode.com/problems/calculate-parking-fees-and-duration">Calculate Parking Fees and Duration</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>ParkingTransactions</code></p>

<pre>
+--------------+-----------+
| Column Name  | Type      |
+--------------+-----------+
| lot_id       | int       |
| car_id       | int       |
| entry_time   | datetime  |
| exit_time    | datetime  |
| fee_paid     | decimal   |
+--------------+-----------+
(lot_id, car_id, entry_time) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the ID of the parking lot, the ID of the car, the entry and exit times, and the fee paid for the parking duration.
</pre>

<p>Write a solution to find the <strong>total parking fee</strong> paid by each car <strong>across all parking lots</strong>, and the <strong>average hourly fee</strong> (rounded to <code>2</code> decimal places) paid by <strong>each</strong> car. Also, find the <strong>parking lot</strong> where each car spent the <strong>most total time</strong>.</p>

<p>Return <em>the result table ordered by </em><code>car_id</code><em><b> </b>in<b> ascending </b></em><em> order.</em></p>

<p><strong>Note:</strong> Test cases are generated in such a way that an individual car cannot be in multiple parking lots at the same time.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<p>ParkingTransactions table:</p>

<pre class="example-io">
+--------+--------+---------------------+---------------------+----------+
| lot_id | car_id | entry_time          | exit_time           | fee_paid |
+--------+--------+---------------------+---------------------+----------+
| 1      | 1001   | 2023-06-01 08:00:00 | 2023-06-01 10:30:00 | 5.00     |
| 1      | 1001   | 2023-06-02 11:00:00 | 2023-06-02 12:45:00 | 3.00     |
| 2      | 1001   | 2023-06-01 10:45:00 | 2023-06-01 12:00:00 | 6.00     |
| 2      | 1002   | 2023-06-01 09:00:00 | 2023-06-01 11:30:00 | 4.00     |
| 3      | 1001   | 2023-06-03 07:00:00 | 2023-06-03 09:00:00 | 4.00     |
| 3      | 1002   | 2023-06-02 12:00:00 | 2023-06-02 14:00:00 | 2.00     |
+--------+--------+---------------------+---------------------+----------+
</pre>

<p><strong>Output:</strong></p>

<pre class="example-io">
+--------+----------------+----------------+---------------+
| car_id | total_fee_paid | avg_hourly_fee | most_time_lot |
+--------+----------------+----------------+---------------+
| 1001   | 18.00          | 2.40           | 1             |
| 1002   | 6.00           | 1.33           | 2             |
+--------+----------------+----------------+---------------+
</pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For car ID 1001:
	<ul>
		<li>From 2023-06-01 08:00:00 to 2023-06-01 10:30:00 in lot 1: 2.5 hours, fee 5.00</li>
		<li>From 2023-06-02 11:00:00 to 2023-06-02 12:45:00 in lot 1: 1.75 hours, fee 3.00</li>
		<li>From 2023-06-01 10:45:00 to 2023-06-01 12:00:00 in lot 2: 1.25 hours, fee 6.00</li>
		<li>From 2023-06-03 07:00:00 to 2023-06-03 09:00:00 in lot 3: 2 hours, fee 4.00</li>
	</ul>
	Total fee paid: 18.00, total hours: 7.5, average hourly fee: 2.40, most time spent in lot 1: 2.5 hours.</li>
	<li>For car ID 1002:
	<ul>
		<li>From 2023-06-01 09:00:00 to 2023-06-01 11:30:00 in lot 2: 2.5 hours, fee 4.00</li>
		<li>From 2023-06-02 12:00:00 to 2023-06-02 14:00:00 in lot 3: 2 hours, fee 2.00</li>
	</ul>
	Total fee paid: 6.00, total hours: 4.5, average hourly fee: 1.33, most time spent in lot 2: 2.5 hours.</li>
</ul>

<p><b>Note:</b> Output table is ordered by car_id in ascending order.</p>
</div>
