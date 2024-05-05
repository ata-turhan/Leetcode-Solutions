<h2><a href="https://leetcode.com/problems/minimum-length-of-anagram-concatenation">Minimum Length of Anagram Concatenation</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You are given a string <code>s</code>, which is known to be a concatenation of <strong>anagrams</strong> of some string <code>t</code>.</p>

<p>Return the <strong>minimum</strong> possible length of the string <code>t</code>.</p>

<p>An <strong>anagram</strong> is a word or phrase formed by rearranging the letters of a word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abba&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>One possible string <code>t</code> could be <code>&quot;ba&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;cdef&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>One possible string <code>t</code> could be <code>&quot;cdef&quot;</code>, notice that <code>t</code> can be equal to <code>s</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consist only of lowercase English letters.</li>
</ul>
