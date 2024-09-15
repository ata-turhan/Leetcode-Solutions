from typing import List

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        stable_mountain_indices: List[int] = []

        # Iterate through the list of heights starting from the second element
        for i, h in enumerate(height[1:], start=1):
            # Check if the previous height exceeds the threshold
            if height[i - 1] > threshold:
                stable_mountain_indices.append(i)

        return stable_mountain_indices
