class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num: int) -> int:
            """
            Helper function to compute the sum of the squares of the digits of the given number.
            """
            total_sum = 0
            while num > 0:
                digit = num % 10
                total_sum += digit ** 2
                num //= 10
            return total_sum

        slow_runner = n
        fast_runner = n

        while fast_runner != 1:
            slow_runner = sum_of_squares(slow_runner)
            fast_runner = sum_of_squares(sum_of_squares(fast_runner))
            
            # If slow_runner meets fast_runner and fast_runner is not 1, there is a cycle.
            if fast_runner != 1 and slow_runner == fast_runner:
                return False

        return True

# Example usage:
# sol = Solution()
# print(sol.isHappy(19))  # Output: True
