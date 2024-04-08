<h2><a href="https://leetcode.com/problems/to-be-or-not-to-be">To Be Or Not To Be</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Write a function&nbsp;<code>expect</code> that helps developers test their code. It should take in any value&nbsp;<code>val</code>&nbsp;and return an object with the following two functions.</p>

<ul>
	<li><code>toBe(val)</code>&nbsp;accepts another value and returns&nbsp;<code>true</code>&nbsp;if the two values&nbsp;<code>===</code>&nbsp;each other. If they are not equal, it should throw an error&nbsp;<code>&quot;Not Equal&quot;</code>.</li>
	<li><code>notToBe(val)</code>&nbsp;accepts another value and returns&nbsp;<code>true</code>&nbsp;if the two values&nbsp;<code>!==</code>&nbsp;each other. If they are equal, it should throw an error&nbsp;<code>&quot;Equal&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> func = () =&gt; expect(5).toBe(5)
<strong>Output:</strong> {&quot;value&quot;: true}
<strong>Explanation:</strong> 5 === 5 so this expression returns true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> func = () =&gt; expect(5).toBe(null)
<strong>Output:</strong> {&quot;error&quot;: &quot;Not Equal&quot;}
<strong>Explanation:</strong> 5 !== null so this expression throw the error &quot;Not Equal&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> func = () =&gt; expect(5).notToBe(null)
<strong>Output:</strong> {&quot;value&quot;: true}
<strong>Explanation:</strong> 5 !== null so this expression returns true.
</pre>
