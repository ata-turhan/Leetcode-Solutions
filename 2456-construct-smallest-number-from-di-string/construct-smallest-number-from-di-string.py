class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def dfs(i, num):
            if i == (len(pattern) + 1):
                return num

            for j in range(1, 10):
                if pattern[i - 1] == "I":
                    if j > int(num[-1]) and str(j) not in num:
                        res = dfs(i + 1, num + str(j))
                        if res:
                            return res
                else:
                    if j < int(num[-1]) and str(j) not in num:
                        res = dfs(i + 1, num + str(j))
                        if res:
                            return res
                        

        for i in range(1, 10):
            res = dfs(1, str(i))
            if res:
                return res

        