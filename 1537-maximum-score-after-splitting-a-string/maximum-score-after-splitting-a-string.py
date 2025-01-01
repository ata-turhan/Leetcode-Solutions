class Solution:
    def maxScore(self, s: str) -> int:
        """
        Calculate the maximum score by splitting the string into two non-empty parts.

        :param s: Binary string consisting of '0's and '1's.
        :return: Maximum score achieved by splitting the string.
        """
        # Initialize prefix and suffix arrays for counting zeros and ones
        prefix_zeros = [0] * len(s)  # Cumulative count of zeros from the left
        suffix_ones = [0] * len(s)   # Cumulative count of ones from the right

        # Calculate prefix sums of zeros
        zero_count = 0
        for i in range(len(s)):
            if s[i] == "0":
                zero_count += 1
            prefix_zeros[i] = zero_count

        # Calculate suffix sums of ones
        one_count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                one_count += 1
            suffix_ones[i] = one_count

        # Compute the maximum score by evaluating all split points
        max_score = 0
        for split_point in range(len(s) - 1):  # Split at each valid point (excluding the last index)
            left_score = prefix_zeros[split_point]  # Zeros in the left part
            right_score = suffix_ones[split_point + 1]  # Ones in the right part
            max_score = max(max_score, left_score + right_score)

        return max_score
