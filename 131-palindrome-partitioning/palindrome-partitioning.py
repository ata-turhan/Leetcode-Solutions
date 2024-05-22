from typing import List

class Solution:
    def dp(self, i: int, s: str, current_partition: List[str]) -> List[List[str]]:
        # Base case: if we've reached the end of the string
        if i == len(s):
            return [current_partition.copy()]

        res = []
        # Try partitioning the string from index i to j
        for j in range(i, len(s)):
            # Check if the substring s[i:j+1] is a palindrome
            if s[i:j+1] == s[i:j+1][::-1]:
                # If it is, add it to the current partition
                current_partition.append(s[i:j+1])
                # Recur to partition the remaining string
                res.extend(self.dp(j + 1, s, current_partition))
                # Backtrack by removing the last added substring
                current_partition.pop()
        return res

    def partition(self, s: str) -> List[List[str]]:
        # Initialize the recursive partitioning with an empty partition list
        return self.dp(0, s, [])
