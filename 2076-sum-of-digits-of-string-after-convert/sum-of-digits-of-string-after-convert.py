class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def sum_of_digits(number):
            """Helper function to calculate the sum of digits of a number."""
            digit_sum = 0
            while number > 0:
                digit_sum += number % 10
                number //= 10
            return digit_sum

        # Convert each letter to its corresponding numeric value
        numeric_representation = []
        for letter in s:
            numeric_representation.append(str(ord(letter) - ord("a") + 1))
        
        # Combine the numeric values into a single integer
        num = int("".join(numeric_representation))

        # Perform the digit sum operation k times
        for _ in range(k):
            num = sum_of_digits(num)

        return num
