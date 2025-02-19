class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if 3 * 2 ** (n - 1) < k:
            return ""

        all_strings = []
        
        def dfs(i, string):
            if i == n:
                all_strings.append(string)
                return

            next_chars = ["a", "b", "c"]
            next_chars.remove(string[-1])
            for next_char in next_chars:
                dfs(i + 1, string + next_char)

        dfs(1, "a")
        dfs(1, "b")
        dfs(1, "c")

        return sorted(all_strings)[k-1]