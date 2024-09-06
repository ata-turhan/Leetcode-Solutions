from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # Calculate the sum of the existing rolls
        sum_existing_rolls: int = sum(rolls)
        len_existing_rolls: int = len(rolls)
        
        # Calculate the total sum required for the entire set of rolls
        total_required_sum: int = mean * (n + len_existing_rolls)
        
        # Calculate the sum that must be provided by the missing rolls
        sum_missing_rolls: int = total_required_sum - sum_existing_rolls
        
        # Check if the sum of missing rolls is within the possible bounds
        if not (n <= sum_missing_rolls <= 6 * n):
            return []

        # Calculate the base value for each missing roll and how many extras are left
        base_value: int = sum_missing_rolls // n
        extra_rolls: int = sum_missing_rolls % n
        
        # Construct the missing rolls list initialized with the base value
        missing_rolls: List[int] = [base_value] * n
        
        # Distribute the extra values across the first few rolls
        for i in range(extra_rolls):
            missing_rolls[i] += 1
        
        return missing_rolls
