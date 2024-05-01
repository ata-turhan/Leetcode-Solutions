class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target_sum = 0
        # Sort the array
        nums.sort()
        # Initialize the result list
        result = []
        # Iterate through the array
        for i in range(len(nums)):
            # If the current number is positive, break the loop
            if nums[i] > 0:
                break
            # Skip duplicate elements
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Initialize two pointers, one from the next element and the other from the end
            left = i + 1
            right = len(nums) - 1
            # Continue until the two pointers meet
            while left < right:
                # Skip duplicate elements
                if left > i+1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                if right < len(nums)-1 and nums[right] == nums[right+1]:
                    right -= 1
                    continue
                # Calculate the sum of three elements
                current_sum = nums[i] + nums[left] + nums[right]
                # If the sum equals the target, add the triplet to the result
                if current_sum == target_sum:
                    result.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                # If the sum is less than the target, move the left pointer to the right
                elif current_sum < target_sum:
                    left += 1
                # If the sum is greater than the target, move the right pointer to the left
                else:
                    right -= 1
        return result
