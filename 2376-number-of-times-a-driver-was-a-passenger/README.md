<h2><a href="https://leetcode.com/problems/number-of-times-a-driver-was-a-passenger">Number of Times a Driver Was a Passenger</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>Rides</code></p>

<pre>
+--------------+------+
| Column Name  | Type |
+--------------+------+
| ride_id      | int  |
| driver_id    | int  |
| passenger_id | int  |
+--------------+------+
ride_id is the column with unique values for this table.
Each row of this table contains the ID of the driver and the ID of the passenger that rode in ride_id.
Note that driver_id != passenger_id.
</pre>

<p>&nbsp;</p>

<p>Write a solution&nbsp;to report the ID of each driver and the number of times they were a passenger.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Rides table:
+---------+-----------+--------------+
| ride_id | driver_id | passenger_id |
+---------+-----------+--------------+
| 1       | 7         | 1            |
| 2       | 7         | 2            |
| 3       | 11        | 1            |
| 4       | 11        | 7            |
| 5       | 11        | 7            |
| 6       | 11        | 3            |
+---------+-----------+--------------+
<strong>Output:</strong> 
+-----------+-----+
| driver_id | cnt |
+-----------+-----+
| 7         | 2   |
| 11        | 0   |
+-----------+-----+
<strong>Explanation:</strong> 
There are two drivers in all the given rides: 7 and 11.
The driver with ID = 7 was a passenger two times.
The driver with ID = 11 was never a passenger.
</pre>
