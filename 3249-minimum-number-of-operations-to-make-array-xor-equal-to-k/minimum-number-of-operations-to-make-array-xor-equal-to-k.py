class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = reduce(lambda a, b:a^b, nums)
        total_bin = bin(total)[2:]
        k_bin = bin(k)[2:]
        count = 0
        while len(total_bin) > len(k_bin):
            k_bin = "0" + k_bin
        while len(total_bin) < len(k_bin):
            total_bin = "0" + total_bin
        for a, b in zip(total_bin, k_bin):
            if a != b:
                count += 1
        return count
        