from typing import List

class Solution:
    def checkIfExist(self, numbers: List[int]) -> bool:
        seen_numbers = set()  # Set to store numbers we've encountered
        
        for number in numbers:
            # Check if the current number's double or half exists in the set
            if number * 2 in seen_numbers or number / 2 in seen_numbers:
                return True
            
            # Add the current number to the set
            seen_numbers.add(number)
        
        return False
