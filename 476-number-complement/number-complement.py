class Solution:
    def findComplement(self, num: int) -> int:
        all_1s = 0
        orig_num = num
        while num > 0:
            num >>= 1
            all_1s <<= 1
            all_1s |= 1
        return all_1s - orig_num