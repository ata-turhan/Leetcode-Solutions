from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(start: int, current_partition: List[str]) -> List[List[str]]:
            # Base case: if we've reached the end of the string
            if start == len(s):
                return [current_partition.copy()]

            res = []
            # Try partitioning the string from index start to end
            for end in range(start, len(s)):
                # Check if the substring s[start:end+1] is a palindrome
                if s[start:end+1] == s[start:end+1][::-1]:
                    # If it is, add it to the current partition
                    current_partition.append(s[start:end+1])
                    # Recur to partition the remaining string
                    res.extend(backtrack(end + 1, current_partition))
                    # Backtrack by removing the last added substring
                    current_partition.pop()
            return res

        # Initialize the recursive partitioning with an empty partition list
        return backtrack(0, [])

# Example usage:
# sol = Solution()
# print(sol.partition("aab"))  # Output: [["a","a","b"],["aa","b"]]
