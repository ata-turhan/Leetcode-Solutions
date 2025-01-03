class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        Counts the number of valid splits in the array such that
        the sum of the left part is greater than or equal to the sum of the right part.

        :param nums: List of integers representing the array.
        :return: Number of valid splits.
        """
        # Calculate half of the total sum to compare against cumulative sums
        total_sum = sum(nums)
        valid_splits = 0
        left_sum = 0

        # Iterate through the array, excluding the last element for splitting
        for i in range(len(nums) - 1):
            left_sum += nums[i]  # Update cumulative sum for the left part
            # Check if the left sum is greater than or equal to the right sum
            if left_sum >= total_sum - left_sum:
                valid_splits += 1

        return valid_splits
