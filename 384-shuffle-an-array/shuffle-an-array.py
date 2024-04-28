import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        """
        Initializes the Solution object with a list of numbers.
        """
        self.original = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and returns it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = self.original.copy()  # Create a copy of the original list
        shuffled = []  # Initialize an empty list to store the shuffled elements
        while nums:
            # Randomly select an index from the remaining elements
            random_index = random.randint(0, len(nums) - 1)
            # Remove the selected element from the list and append it to the shuffled list
            shuffled.append(nums.pop(random_index))
        return shuffled

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
