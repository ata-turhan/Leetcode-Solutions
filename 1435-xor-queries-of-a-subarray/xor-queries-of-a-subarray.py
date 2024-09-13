class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        xor_val = 0
        for num in arr:
            xor_val ^= num
            prefix_xor.append(xor_val)

        res = []
        for start, end in queries:
            res.append(prefix_xor[end+1] ^ prefix_xor[start])

        return res

        