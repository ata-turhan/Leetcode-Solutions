from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        
        # Calculate the potential gain for each node when its value is XORed with k
        potentialGain = [(nums[i] ^ k) - nums[i] for i in range(n)]
        
        # Start with the initial sum of all node values
        totalValue = sum(nums)

        # Sort potential gains in descending order to maximize the positive impact
        potentialGain.sort(reverse=True)

        # Process the sorted potential gains in pairs
        for i in range(0, n, 2):
            # If potentialGain contains an odd number of elements, handle the last element separately
            if i + 1 >= n:
                break
            combinedGain = potentialGain[i] + potentialGain[i + 1]
            # Include in totalValue if combinedGain is positive
            if combinedGain > 0:
                totalValue += combinedGain
            else:
                break

        return totalValue
