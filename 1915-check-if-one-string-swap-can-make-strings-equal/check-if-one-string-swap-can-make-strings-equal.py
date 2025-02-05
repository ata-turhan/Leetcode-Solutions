class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Checks if two strings can be made equal by swapping exactly one pair of characters.

        :param s1: First input string.
        :param s2: Second input string.
        :return: True if the strings can be made equal by one swap, otherwise False.
        """
        mismatch_indices = []  # Stores indices where characters differ

        # Identify mismatched indices
        for index in range(len(s1)):
            if s1[index] != s2[index]:
                mismatch_indices.append(index)

        # If no mismatches, strings are already equal
        if not mismatch_indices:
            return True

        # If more than 2 mismatches, one swap cannot fix it
        if len(mismatch_indices) != 2:
            return False

        # Check if swapping the mismatched characters would make the strings equal
        first_idx, second_idx = mismatch_indices
        return s1[first_idx] == s2[second_idx] and s1[second_idx] == s2[first_idx]
