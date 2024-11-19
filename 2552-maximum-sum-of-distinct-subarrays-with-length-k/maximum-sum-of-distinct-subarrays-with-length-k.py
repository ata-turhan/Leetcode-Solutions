from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        distinct_count = 0  # Tracks the count of distinct numbers in the window
        current_sum = 0  # Tracks the sum of the current window
        max_sum = 0  # Tracks the maximum sum of a valid subarray
        num_count = defaultdict(int)  # Dictionary to store the count of each number in the window

        # Initialize the window for the first k-1 elements
        for i in range(k - 1):
            if num_count[nums[i]] == 0:
                distinct_count += 1
            num_count[nums[i]] += 1
            current_sum += nums[i]

        # Slide the window through the array
        for i in range(k - 1, len(nums)):
            # Add the current number to the window
            if num_count[nums[i]] == 0:
                distinct_count += 1
            num_count[nums[i]] += 1
            current_sum += nums[i]

            # Check if the current window has k distinct elements
            if distinct_count == k:
                max_sum = max(max_sum, current_sum)

            # Remove the oldest number from the window
            num_count[nums[i - k + 1]] -= 1
            if num_count[nums[i - k + 1]] == 0:
                distinct_count -= 1
            current_sum -= nums[i - k + 1]

        return max_sum
