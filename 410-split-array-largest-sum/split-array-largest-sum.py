from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Function to split the array into subarrays with maximum sum no greater than max_val
        def split(max_val, m):
            cur_sum = 0
            subarray_count = 1
            for num in nums:
                # Add the current number to the current subarray if adding it doesn't exceed max_val
                if cur_sum + num <= max_val:
                    cur_sum += num
                # Otherwise, start a new subarray with the current number
                else:
                    cur_sum = num
                    subarray_count += 1
                    # If the number of subarrays exceeds m, return infinity
                    if subarray_count > m:
                        return float("inf")
            return subarray_count

        # Initialize the search range for the maximum subarray sum
        left = max(nums)
        right = sum(nums)
        min_sum = float("inf")
        
        # Perform binary search to find the minimum sum that satisfies the conditions
        while left <= right:
            mid = left + (right - left) // 2
            subarray_count = split(mid, m)
            if subarray_count <= m:
                # If the number of subarrays is less than or equal to m, update min_sum and move left pointer
                right = mid - 1
                min_sum = min(min_sum, mid)
            else:
                # If the number of subarrays exceeds m, move right pointer
                left = mid + 1
        return min_sum
