class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        Count the number of good strings that can be formed using the given rules.
        
        A good string has a length between 'low' and 'high' inclusive, and can only be formed
        by appending 'zero' or 'one' characters repeatedly to an empty string.

        :param low: Minimum length of the string.
        :param high: Maximum length of the string.
        :param zero: Number of characters to append for a '0' operation.
        :param one: Number of characters to append for a '1' operation.
        :return: The count of good strings modulo 10^9 + 7.
        """
        MODULO = 10**9 + 7

        @cache
        def count_ways(current_length: int) -> int:
            """
            Recursive function with memoization to count good strings starting from a given length.

            :param current_length: Current length of the string being formed.
            :return: Count of good strings that can be formed starting from this length.
            """
            # Base case: If the current length exceeds 'high', no more valid strings can be formed
            if current_length > high:
                return 0

            # Initialize the number of ways to form good strings from the current length
            ways = 0

            # If the current length is within the valid range, count it as a good string
            if low <= current_length <= high:
                ways += 1

            # Recursive calls to form strings by appending 'zero' or 'one' characters
            ways += count_ways(current_length + zero)
            ways += count_ways(current_length + one)

            # Return the total number of ways modulo 10^9 + 7
            return ways % MODULO

        # Start the recursive process from length 0
        return count_ways(0)
