from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # Helper function to calculate the OR value from the bit counts array
        def calculate_or_from_bits(bit_counts):
            or_result = 0
            for bit_position in range(64):
                # If any number has this bit set, include it in the OR result
                if bit_counts[bit_position] > 0:
                    or_result += 2 ** bit_position
            return or_result

        bit_counts = [0] * 64  # Tracks counts of set bits at each position in the window
        current_or_value = 0
        left_pointer = 0
        minimum_length = len(nums) + 1  # Initialize with a value larger than any possible subarray

        # Expand the right pointer to include each element in the window
        for right_pointer in range(len(nums)):
            bit_index = 0
            number = nums[right_pointer]

            # Update bit counts for the current number
            while number > 0:
                if number & 1:
                    bit_counts[bit_index] += 1
                bit_index += 1
                number >>= 1

            # Recalculate OR value for the current window
            current_or_value = calculate_or_from_bits(bit_counts)

            # Contract the window from the left until OR value is less than k
            while left_pointer <= right_pointer and current_or_value >= k:
                # Update minimum length of valid subarrays
                minimum_length = min(minimum_length, right_pointer - left_pointer + 1)

                # Remove the leftmost element's bit contribution
                bit_index = 0
                number = nums[left_pointer]
                while number > 0:
                    if number & 1:
                        bit_counts[bit_index] -= 1
                    bit_index += 1
                    number >>= 1

                # Recalculate OR value after adjusting bit counts
                current_or_value = calculate_or_from_bits(bit_counts)
                left_pointer += 1  # Move the left pointer to the right

        # Return the minimum subarray length, or -1 if no valid subarray found
        return -1 if minimum_length == len(nums) + 1 else minimum_length
