from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Initialize the result list and convert wordDict to a set for O(1) lookups
        res = []
        wordDict = set(wordDict)

        def backtrack(i, j, array):
            # Base case: If we have reached the end of the string
            if j == len(s) - 1:
                # Check if the current substring is in the wordDict
                if s[i:j + 1] in wordDict:
                    array.append(s[i:j + 1])
                    res.append(" ".join(array))
                    array.pop()
                return

            # If the current substring is in the wordDict, proceed with backtracking
            if s[i:j + 1] in wordDict:
                array.append(s[i:j + 1])
                backtrack(j + 1, j + 1, array)
                array.pop()
                backtrack(i, j + 1, array)
            else:
                backtrack(i, j + 1, array)

        # Start the backtracking process
        backtrack(0, 0, [])
        return res

# Example usage:
# sol = Solution()
# print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))  
# Output: ["cats and dog", "cat sand dog"]
