class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive_odd_count = 0  # Track the number of consecutive odd numbers

        for num in arr:
            if num % 2 == 0:
                # Reset the count if the current number is even
                consecutive_odd_count = 0
            else:
                # Increment the count if the current number is odd
                consecutive_odd_count += 1

            # Check if there are three consecutive odd numbers
            if consecutive_odd_count == 3:
                return True

        # Return False if no three consecutive odd numbers are found
        return False
