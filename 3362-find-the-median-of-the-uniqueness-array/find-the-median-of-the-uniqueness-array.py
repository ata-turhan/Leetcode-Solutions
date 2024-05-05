from collections import defaultdict
from typing import List

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        # Calculate the total possible unique sums
        total_unique_sums: int = len(nums) * (len(nums) + 1) // 2

        def count_at_most(k: int) -> int:
            """
            Count the number of subarrays with at most k unique elements.
            """
            count: defaultdict[int, int] = defaultdict(int)  # Track the count of each unique element
            left: int = 0
            res: int = 0  # Initialize left pointer and result counter
            
            # Iterate through the array using two pointers
            for right in range(len(nums)):
                # Increment count for the current element
                count[nums[right]] += 1
                
                # Adjust the left pointer if the count exceeds k
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                
                # Add the count of subarrays with at most k unique elements
                res += right - left + 1
            return res

        # Binary search for the minimum k
        left: int = 1
        right: int = len(set(nums))
        while left < right:
            mid: int = (left + right) // 2
            # If the count of subarrays with at most k unique elements
            # is at least half of the total possible unique sums,
            # then set the upper bound to mid, else set the lower bound to mid + 1
            if count_at_most(mid) * 2 >= total_unique_sums:
                right = mid
            else:
                left = mid + 1
        return left
