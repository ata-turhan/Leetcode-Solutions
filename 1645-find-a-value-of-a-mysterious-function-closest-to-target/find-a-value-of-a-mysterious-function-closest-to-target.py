from typing import List, Dict
from collections import Counter

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        """
        Finds the subarray with the bitwise AND value closest to the target.
        
        :param arr: List[int] - The input list of integers.
        :param target: int - The target integer.
        :return: int - The minimum difference between any subarray's bitwise AND value and the target.
        """
        def getSetBitsPositions(x: int) -> List[int]:
            """
            Returns the positions of set bits in the binary representation of x.
            
            :param x: int - The input integer.
            :return: List[int] - List of positions of set bits.
            """
            return [i for i, bit in enumerate(reversed(bin(x)[2:])) if bit == '1']

        def calculateBitwiseAND(window_length: int, bit_counts: Dict[int, int]) -> int:
            """
            Computes the bitwise AND value from the bit counts.
            
            :param window_length: int - The length of the current window.
            :param bit_counts: Dict[int, int] - The counts of set bits.
            :return: int - The computed bitwise AND value.
            """
            return sum((1 << bit_position) for bit_position, count in bit_counts.items() if count == window_length)

        current_and_value = arr[0]  # Initialize current AND value with the first number
        minimum_difference = abs(current_and_value - target)  # Initialize the minimum difference

        window_bit_counts = Counter(getSetBitsPositions(arr[0]))  # Initialize the bit counts for the first number

        left_pointer = right_pointer = 0  # Initialize left and right pointers

        # Iterate through the array using a sliding window approach
        while right_pointer < len(arr):
            if current_and_value > target or left_pointer > right_pointer:
                # Expand the window to the right
                right_pointer += 1
                if right_pointer >= len(arr):
                    break
                window_bit_counts += Counter(getSetBitsPositions(arr[right_pointer]))
            else:
                # Shrink the window from the left
                window_bit_counts -= Counter(getSetBitsPositions(arr[left_pointer]))
                left_pointer += 1

            current_and_value = calculateBitwiseAND(right_pointer - left_pointer + 1, window_bit_counts)  # Compute the current AND value

            if left_pointer <= right_pointer:
                minimum_difference = min(minimum_difference, abs(current_and_value - target))  # Update the minimum difference

        return minimum_difference  # Return the minimum difference

# Example usage:
# sol = Solution()
# print(sol.closestToTarget([1, 2, 3, 4], 1))  # Output: 0
# print(sol.closestToTarget([4, 2, 7, 1], 3))  # Output: 0
