from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)  # dp[i] will be the minimum height for the first i books
        dp[0] = 0  # Base case: no books, no height

        for i in range(1, n + 1):
            width = 0
            height = 0
            # Try to place books[i-1] to books[j-1] on the same shelf
            for j in range(i, 0, -1):
                width += books[j-1][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1] + height)

        return dp[n]
