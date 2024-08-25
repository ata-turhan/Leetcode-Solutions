from collections import Counter, defaultdict
from itertools import combinations
from typing import List

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        MAX_DIGITS = 7  # Maximum number of digits in nums[i] since 1 <= nums[i] < 10^7

        num_count = Counter(nums)  # Count occurrences of each number in nums
        possible_pairs = defaultdict(list)  # Store possible pairings of numbers
        
        # Populate the possible_pairs map with potential pair candidates
        for num, count in num_count.items(): 
            possible_pairs[num].append((num, count))
            num_str = list(str(num).zfill(MAX_DIGITS))  # Convert the number to a zero-padded string of length MAX_DIGITS
            for i in range(MAX_DIGITS): 
                for j in range(i + 1, MAX_DIGITS): 
                    if num_str[i] != num_str[j]: 
                        # Swap two different digits
                        num_str[i], num_str[j] = num_str[j], num_str[i]
                        candidate = int("".join(num_str))  # Create a candidate number from the modified string
                        possible_pairs[candidate].append((num, count))  # Store the original number and its count in possible_pairs
                        # Swap back to restore the original configuration for further modifications
                        num_str[i], num_str[j] = num_str[j], num_str[i]
        
        pair_count = defaultdict(int)
        
        # Calculate the number of valid pairs based on the possible_pairs map
        for candidate, values in possible_pairs.items(): 
            # Count pairs within the same number (num1 == num2)
            for num1, count1 in values: 
                pair_count[(num1, num1)] = count1 * (count1 - 1) // 2  # Combinatorial count for the same number
            
            # Count pairs between different numbers (num1 != num2)
            for (num1, count1), (num2, count2) in combinations(values, 2): 
                pair_count[(num1, num2)] = count1 * count2  # Count pairs between different numbers
        
        return sum(pair_count.values())  # Sum up all counted pairs and return the total
