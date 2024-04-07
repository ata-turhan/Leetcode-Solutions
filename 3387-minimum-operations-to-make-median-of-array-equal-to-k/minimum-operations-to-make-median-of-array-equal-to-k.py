class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the list
        med_idx = len(nums) // 2  # Calculate the index of the median
        res = 0  # Initialize the result

        # Check if median is equal to k
        if nums[med_idx] == k:
            return 0
        # If median is less than k, iterate from median towards end of list
        elif nums[med_idx] < k:
            res += k - nums[med_idx] 
            for i in range(med_idx + 1, len(nums)):
                if nums[i] < k:
                    res += k - nums[i]
                else:
                    return res
            return res
        # If median is greater than k, iterate from median towards start of list
        elif nums[med_idx] > k:
            res += nums[med_idx] - k 
            for i in range(med_idx - 1, -1, -1):
                if nums[i] > k:
                    res += nums[i] - k
                else:
                    return res
            return res
