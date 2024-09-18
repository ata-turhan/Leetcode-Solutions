from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a: str, b: str) -> int:
            # Compare by concatenating in both possible orders
            if a + b > b + a:
                return -1  # `a` should come before `b`
            elif a + b < b + a:
                return 1   # `b` should come before `a`
            else:
                return 0   # `a` and `b` are equal in comparison

        # Convert all integers to strings
        str_nums = [str(num) for num in nums]
        # Sort using the custom comparator
        str_nums.sort(key=cmp_to_key(compare))

        # Join sorted numbers and handle the edge case where the largest number is "0"
        largest_number = "".join(str_nums)
        return "0" if largest_number[0] == "0" else largest_number
