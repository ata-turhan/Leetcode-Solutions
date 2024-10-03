class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target_rem = total_sum % p

        if target_rem == 0:
            return 0

        remainder_map = {0: -1}
        current_sum = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            current_sum += num
            current_rem = current_sum % p
            needed_rem = (current_rem - target_rem) % p

            if needed_rem in remainder_map:
                subarray_len = i - remainder_map[needed_rem]
                if subarray_len < len(nums):
                    min_len = min(min_len, subarray_len)

            remainder_map[current_rem] = i

        return min_len if min_len < len(nums) else -1
