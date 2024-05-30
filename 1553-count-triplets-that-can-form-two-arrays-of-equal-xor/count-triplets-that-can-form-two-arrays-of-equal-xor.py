class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_xors = [0]
        xor_val = 0
        for num in arr:
            xor_val ^= num
            prefix_xors.append(xor_val)

        res = 0
        for i in range(len(prefix_xors)-2):
            for j in range(i+2, len(prefix_xors)):
                if prefix_xors[i] ^ prefix_xors[j] == 0:
                    res += j - i - 1

        return res
        