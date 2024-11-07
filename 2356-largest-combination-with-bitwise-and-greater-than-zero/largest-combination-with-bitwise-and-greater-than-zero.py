class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_num = max(candidates)
        max_bit_count = len(bin(max_num)) - 2
        max_count = 0

        for set_bit in range(max_bit_count):
            count = 0
            for num in candidates:
                if (num >> set_bit) & 1:
                    count += 1
            print(count, set_bit)
            max_count = max(max_count, count)

        return max_count
        