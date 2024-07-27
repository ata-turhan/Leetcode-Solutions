from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """
        Counts the number of triplets (i, j, k) such that the XOR from arr[i] to arr[j-1]
        is equal to the XOR from arr[j] to arr[k].

        :param arr: List[int] - The input array of integers.
        :return: int - The number of valid triplets.
        """
        prefix_xors = [0]  # Initialize prefix XORs with a starting value of 0
        xor_val = 0  # Initialize the XOR accumulator

        # Compute the prefix XORs
        for num in arr:
            xor_val ^= num  # Compute the cumulative XOR up to the current element
            prefix_xors.append(xor_val)  # Append the current XOR value to the prefix XOR list

        res = 0  # Initialize the result counter

        # Iterate over all possible pairs (i, j) to find valid triplets
        for i in range(len(prefix_xors) - 2):
            for k in range(i + 2, len(prefix_xors)):
                # Check if the XOR from prefix_xors[i] to prefix_xors[k] is 0
                if prefix_xors[i] ^ prefix_xors[k] == 0:
                    res += k - i - 1  # Increment the result by the number of valid j values

        return res  # Return the total number of valid triplets

# Example usage:
# sol = Solution()
# print(sol.countTriplets([2, 3, 1, 6, 7]))  # Output: 4
# print(sol.countTriplets([1, 1, 1, 1, 1]))  # Output: 10
