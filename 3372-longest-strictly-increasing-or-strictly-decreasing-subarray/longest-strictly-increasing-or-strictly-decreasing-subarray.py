class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Initialize variables for maximum length and current length of monotonic subarray
        max_length = 1
        cur_length = 1
        
        # Flags to track monotonicity
        increasing = decreasing = False

        # Iterate through the list
        for i in range(1, len(nums)):
            # Check if current number is greater than previous number
            if nums[i] > nums[i-1]:
                increasing = True
                # If previously decreasing, reset current length to 2, otherwise increment
                if decreasing:
                    cur_length = 2
                    decreasing = False
                else:
                    cur_length += 1
            # Check if current number is less than previous number
            elif nums[i] < nums[i-1]:
                decreasing = True
                # If previously increasing, reset current length to 2, otherwise increment
                if increasing:
                    cur_length = 2
                    increasing = False
                else:
                    cur_length += 1
            # If current number is equal to previous number, reset current length and flags
            else:
                cur_length = 1
                increasing = decreasing = False

            # Update maximum length
            max_length = max(max_length, cur_length)

        return max_length
