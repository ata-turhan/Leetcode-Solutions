from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # Create a copy of the energy list to store the dynamic programming values
        dp = energy.copy()
        
        # Iterate backward through the energy list
        for i in range(len(energy)-1, -1, -1):
            # Calculate the cumulative energy starting from the current index
            cumulative_energy = dp[i+k] if i + k < len(energy) else 0
            # Update the dynamic programming value for the current index
            dp[i] += cumulative_energy

        # Return the maximum energy value from the dynamic programming list
        return max(dp)


        ##### prefix sum solution

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
