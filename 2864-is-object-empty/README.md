<h2><a href="https://leetcode.com/problems/is-object-empty">Is Object Empty</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an object or an array, return if it is empty.</p>

<ul>
	<li>An empty object contains no key-value pairs.</li>
	<li>An empty array contains no elements.</li>
</ul>

<p>You may assume the object or array is the output of&nbsp;<code>JSON.parse</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> obj = {&quot;x&quot;: 5, &quot;y&quot;: 42}
<strong>Output:</strong> false
<strong>Explanation:</strong> The object has 2 key-value pairs so it is not empty.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> obj = {}
<strong>Output:</strong> true
<strong>Explanation:</strong> The object doesn&#39;t have any key-value pairs so it is empty.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> obj = [null, false, 0]
<strong>Output:</strong> false
<strong>Explanation:</strong> The array has 3 elements so it is not empty.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>obj</code> is a valid JSON object or array</li>
	<li><code>2 &lt;= JSON.stringify(obj).length &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Can you solve it in O(1) time?</strong>