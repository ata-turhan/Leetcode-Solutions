class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # Perform binary search until left pointer exceeds the right pointer.
        while left <= right:            
            mid = left + (right - left) // 2

            # Check if the middle element is greater than the rightmost element.
            if nums[mid] > nums[right]:
                # If so, the minimum element must be in the right half.
                left = mid + 1
            elif nums[mid] < nums[right]:
                # If the middle element is less than the rightmost element,
                # the minimum element must be in the left half.
                right = mid 
            else:
                # If the middle element is equal to the rightmost element,
                # we decrease the search range by adjusting the right pointer.
                right -= 1

        # At the end of the loop, left pointer points to the minimum element.
        return nums[left]
