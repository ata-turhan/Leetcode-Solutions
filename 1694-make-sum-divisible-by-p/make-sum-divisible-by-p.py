from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target_rem = total_sum % p  # Remainder we want to remove

        # If the total sum is already divisible by p, return 0
        if target_rem == 0:
            return 0

        remainder_map = {0: -1}  # To store prefix sum remainders
        current_sum = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            current_sum += num
            current_rem = current_sum % p
            needed_rem = (current_rem - target_rem) % p  # Remainder needed to make the sum divisible

            # If the needed remainder was seen before, calculate the subarray length
            if needed_rem in remainder_map:
                subarray_len = i - remainder_map[needed_rem]
                # Update the minimum subarray length
                min_len = min(min_len, subarray_len)

            # Store the current remainder with its index
            remainder_map[current_rem] = i

        # Return the minimum length if it's valid, otherwise return -1
        return min_len if min_len < len(nums) else -1
