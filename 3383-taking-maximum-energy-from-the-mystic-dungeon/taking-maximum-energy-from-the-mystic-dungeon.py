from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # Initialize a list to store the maximum energy sums for each possible starting point
        max_energy_sums = []
        # Iterate over the possible starting points
        for i in range(k):
            # Initialize a list to store the energy values for the current starting point
            val = []
            # Iterate over the energy values for the current starting point
            for j in range(i, len(energy), k):
                val.append(energy[j])
            # Calculate the cumulative energy sums from right to left
            for j in range(len(val)-2, -1, -1):
                val[j] += val[j+1] 
            # Add the energy values for the current starting point to the list of maximum energy sums
            max_energy_sums.extend(val)
        # Return the maximum energy sum among all possible starting points
        return max(max_energy_sums)
