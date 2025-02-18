class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
        Generates the lexicographically smallest number that follows 
        the given pattern of 'I' (increasing) and 'D' (decreasing).
        """

        def backtrack(index: int, current_num: str) -> str:
            """
            Backtracking function to construct the smallest valid number.
            - `index`: Current position in the pattern.
            - `current_num`: The number sequence formed so far.
            """

            # Base case: If all digits are placed, return the number
            if index == len(pattern) + 1:
                return current_num

            for digit in range(1, 10):
                last_digit = int(current_num[-1])

                # 'I' condition: next digit must be greater
                if pattern[index - 1] == "I" and digit > last_digit and str(digit) not in current_num:
                    result = backtrack(index + 1, current_num + str(digit))
                    if result:
                        return result

                # 'D' condition: next digit must be smaller
                elif pattern[index - 1] == "D" and digit < last_digit and str(digit) not in current_num:
                    result = backtrack(index + 1, current_num + str(digit))
                    if result:
                        return result

        # Try all digits (1-9) as starting points
        for start_digit in range(1, 10):
            result = backtrack(1, str(start_digit))
            if result:
                return result
