class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0  # If there's only one element, it's the peak

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if the mid element is a peak
            if mid == 0 and nums[mid] > nums[mid + 1]:
                return mid
            if mid == len(nums) - 1 and nums[mid] > nums[mid - 1]:
                return mid
            if 0 < mid < len(nums) - 1 and nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            # Move towards the direction of the higher adjacent element
            if nums[mid + 1] < nums[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1

        return -1  # In case no peak is found, although it shouldn't happen
