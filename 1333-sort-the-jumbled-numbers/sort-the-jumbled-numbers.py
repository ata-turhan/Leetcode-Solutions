from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def get_mapped_value(num: int) -> int:
            # Convert the number to its mapped value according to the given mapping
            mapped_value = ""
            for digit in str(num):
                mapped_value += str(mapping[int(digit)])
            return int(mapped_value)
        
        # Sort the nums list based on their mapped values
        nums.sort(key=lambda num: get_mapped_value(num))
        
        return nums
