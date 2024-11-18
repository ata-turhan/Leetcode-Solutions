class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        n = len(code)
        code.extend(code)

        if k > 0:
            cur_sum = sum(code[1:k])
            res = []
            for i in range(k, n + k):
                cur_sum += code[i]
                res.append(cur_sum)
                cur_sum -= code[i-k+1]
        else:
            k = -k
            cur_sum = sum(code[n-k:n-1])
            res = []
            for i in range(n-1, 2 * n - 1):
                cur_sum += code[i]
                res.append(cur_sum)
                cur_sum -= code[i-k+1]

        return res
        