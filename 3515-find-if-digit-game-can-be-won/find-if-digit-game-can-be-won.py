class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        total_sum = sum(nums)  # Calculate the total sum of all numbers
        
        # Calculate the sum of single-digit numbers
        single_digit_sum = sum(num for num in nums if num < 10)
        
        # Calculate the sum of double-digit numbers
        double_digit_sum = total_sum - single_digit_sum
        
        # Alice can win if the sum of single-digit numbers is not equal to the sum of double-digit numbers
        return single_digit_sum != double_digit_sum
