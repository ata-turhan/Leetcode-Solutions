from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize the array with the first element of nums
        arr = [nums.pop(0)]  # Step 1: Initial step
        
        # Iterate through the remaining elements in nums
        for n in nums:  # Step 2: Iterate through nums
            
            if n > arr[-1]:  # Step 2a: If n is greater than the last element in arr
                arr.append(n)  # Append n to arr

            else:  # Step 2b: If n is not greater than the last element in arr
                # Find the position to replace in arr using binary search
                arr[bisect_left(arr, n)] = n

        return len(arr)  # Return the length of arr which represents the length of LIS
