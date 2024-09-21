from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result: List[int] = []

        # Depth-first search function to build the numbers in lexical order
        def dfs(current: int):
            if current > n:
                return
            result.append(current)  # Add the current number to the result list
            for i in range(10):  # Explore next digits
                next_num: int = current * 10 + i  # Generate the next number
                if next_num > n:
                    break
                dfs(next_num)  # Recursively call dfs for the next number

        # Start DFS for each number from 1 to 9 (lexical order starts with these)
        for i in range(1, 10):
            dfs(i)

        return result
