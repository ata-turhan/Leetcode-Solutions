from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Finds the majority element in a list, which is the element that appears more than n // 2 times.
        
        :param nums: List[int] - List of integers.
        :return: int - The majority element.
        """
        # Create a Counter object to count the frequency of each element
        counts = Counter(nums)
        
        # Find the element with the maximum frequency
        return max(counts.items(), key=lambda x: x[1])[0]

# Example usage:
# sol = Solution()
# print(sol.majorityElement([3, 2, 3]))  # Output: 3
# print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
