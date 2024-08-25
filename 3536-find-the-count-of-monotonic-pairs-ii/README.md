<h2><a href="https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii">Find the Count of Monotonic Pairs II</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><p>You are given an array of <strong>positive</strong> integers <code>nums</code> of length <code>n</code>.</p>

<p>We call a pair of <strong>non-negative</strong> integer arrays <code>(arr1, arr2)</code> <strong>monotonic</strong> if:</p>

<ul>
	<li>The lengths of both arrays are <code>n</code>.</li>
	<li><code>arr1</code> is monotonically <strong>non-decreasing</strong>, in other words, <code>arr1[0] &lt;= arr1[1] &lt;= ... &lt;= arr1[n - 1]</code>.</li>
	<li><code>arr2</code> is monotonically <strong>non-increasing</strong>, in other words, <code>arr2[0] &gt;= arr2[1] &gt;= ... &gt;= arr2[n - 1]</code>.</li>
	<li><code>arr1[i] + arr2[i] == nums[i]</code> for all <code>0 &lt;= i &lt;= n - 1</code>.</li>
</ul>

<p>Return the count of <strong>monotonic</strong> pairs.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The good pairs are:</p>

<ol>
	<li><code>([0, 1, 1], [2, 2, 1])</code></li>
	<li><code>([0, 1, 2], [2, 2, 0])</code></li>
	<li><code>([0, 2, 2], [2, 1, 0])</code></li>
	<li><code>([1, 2, 2], [1, 1, 0])</code></li>
</ol>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,5,5,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">126</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 2000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>
