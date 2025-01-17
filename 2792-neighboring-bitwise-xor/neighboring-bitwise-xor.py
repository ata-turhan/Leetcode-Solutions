from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
        Check if a valid original array exists based on the given derived array.
        
        :param derived: List[int] - The derived array where derived[i] is the XOR of original[i] and original[i+1].
        :return: bool - True if a valid original array exists, False otherwise.
        """
        # Initialize the original array starting with the first element as 1
        original_array = [1]

        # Reconstruct the original array based on the derived array
        for i in range(len(derived) - 1):
            if derived[i] == 1:
                # If derived[i] is 1, flip the last element to get the next element
                original_array.append(1 - original_array[-1])
            else:
                # If derived[i] is 0, repeat the last element
                original_array.append(original_array[-1])

        # Check if the XOR of the first and last element matches derived[-1]
        return (original_array[0] ^ original_array[-1]) == derived[-1]
