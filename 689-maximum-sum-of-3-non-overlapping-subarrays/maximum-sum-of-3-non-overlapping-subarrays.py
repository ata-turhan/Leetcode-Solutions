class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        Find starting indices of three non-overlapping subarrays of length k that maximize their total sum.

        :param nums: List of integers representing the array.
        :param k: Length of each subarray.
        :return: List of three starting indices of the subarrays.
        """
        # Variables to track the best starting indices for one, two, and three subarray configurations
        best_one_start = 0  # Best starting index for a single subarray
        best_two_start = [0, k]  # Best starting indices for two subarrays
        best_three_start = [0, k, 2 * k]  # Best starting indices for three subarrays

        # Compute initial sums for the first subarrays
        one_sum = sum(nums[:k])  # Sum of the first subarray
        two_sum = sum(nums[k:2 * k])  # Sum of the second subarray
        three_sum = sum(nums[2 * k:3 * k])  # Sum of the third subarray

        # Track the best sums found so far
        max_one_sum = one_sum
        max_two_sum = one_sum + two_sum
        max_three_sum = one_sum + two_sum + three_sum

        # Sliding window pointers for the subarrays
        single_start = 1
        double_start = k + 1
        triple_start = 2 * k + 1

        # Slide the windows across the array
        while triple_start <= len(nums) - k:
            # Update sums using sliding window technique
            one_sum = one_sum - nums[single_start - 1] + nums[single_start + k - 1]
            two_sum = two_sum - nums[double_start - 1] + nums[double_start + k - 1]
            three_sum = three_sum - nums[triple_start - 1] + nums[triple_start + k - 1]

            # Update best index for a single subarray if a better sum is found
            if one_sum > max_one_sum:
                best_one_start = single_start
                max_one_sum = one_sum

            # Update best indices for two subarrays if a better sum is found
            if two_sum + max_one_sum > max_two_sum:
                best_two_start = [best_one_start, double_start]
                max_two_sum = two_sum + max_one_sum

            # Update best indices for three subarrays if a better sum is found
            if three_sum + max_two_sum > max_three_sum:
                best_three_start = [best_two_start[0], best_two_start[1], triple_start]
                max_three_sum = three_sum + max_two_sum

            # Move the sliding windows forward
            single_start += 1
            double_start += 1
            triple_start += 1

        # Return the starting indices of the three subarrays with the maximum sum
        return best_three_start
