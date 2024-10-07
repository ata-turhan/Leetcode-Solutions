<h2><a href="https://leetcode.com/problems/dynamic-pivoting-of-a-table">Dynamic Pivoting of a Table</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><p>Table: <code>Products</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store       | varchar |
| price       | int     |
+-------------+---------+
(product_id, store) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the price of product_id in store.
There will be at most 30 different stores in the table.
price is the price of the product at this store.
</pre>

<p>&nbsp;</p>

<p><strong>Important note:</strong> This problem targets those who have a good experience with SQL. If you are a beginner, we recommend that you skip it for now.</p>

<p>Implement the procedure <code>PivotProducts</code> to reorganize the <code>Products</code> table so that each row has the id of one product and its price in each store. The price should be <code>null</code> if the product is not sold in a store. The columns of the table should contain each store and they should be sorted in <strong>lexicographical order</strong>.</p>

<p>The procedure should return the table after reorganizing it.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Products table:
+------------+----------+-------+
| product_id | store    | price |
+------------+----------+-------+
| 1          | Shop     | 110   |
| 1          | LC_Store | 100   |
| 2          | Nozama   | 200   |
| 2          | Souq     | 190   |
| 3          | Shop     | 1000  |
| 3          | Souq     | 1900  |
+------------+----------+-------+
<strong>Output:</strong> 
+------------+----------+--------+------+------+
| product_id | LC_Store | Nozama | Shop | Souq |
+------------+----------+--------+------+------+
| 1          | 100      | null   | 110  | null |
| 2          | null     | 200    | null | 190  |
| 3          | null     | null   | 1000 | 1900 |
+------------+----------+--------+------+------+
<strong>Explanation:</strong> 
We have 4 stores: Shop, LC_Store, Nozama, and Souq. We first order them lexicographically to be: LC_Store, Nozama, Shop, and Souq.
Now, for product 1, the price in LC_Store is 100 and in Shop is 110. For the other two stores, the product is not sold so we set the price as null.
Similarly, product 2 has a price of 200 in Nozama and 190 in Souq. It is not sold in the other two stores.
For product 3, the price is 1000 in Shop and 1900 in Souq. It is not sold in the other two stores.
</pre>
