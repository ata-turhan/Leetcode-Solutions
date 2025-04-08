from typing import List
from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Computes the minimum number of operations needed to remove duplicates from nums
        using a batch of 3-element deletions per operation. Each operation removes 3 elements.
        Returns the number of operations required to make all elements distinct.
        """

        frequency = Counter(nums)
        duplicate_count = sum(1 for count in frequency.values() if count > 1)
        num_operations = 0
        nums = nums[::-1]  # Reverse to simulate popping from the end

        while duplicate_count > 0:
            if len(nums) <= 3:
                num_operations += 1
                break

            # Remove up to 3 elements from the end
            for _ in range(3):
                if not nums:
                    break
                val = nums.pop()
                frequency[val] -= 1
                if frequency[val] == 1:
                    duplicate_count -= 1

            num_operations += 1

        return num_operations
