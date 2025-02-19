class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Generates the k-th lexicographically smallest happy string of length `n`.
        A happy string is a string where no two adjacent characters are the same.
        """

        # Maximum possible happy strings of length `n` is 3 * 2^(n-1)
        max_happy_strings = 3 * (2 ** (n - 1))
        if k > max_happy_strings:
            return ""  # Return empty string if `k` is out of range

        happy_strings = []  # Stores all valid happy strings

        def backtrack(index: int, current_string: str) -> None:
            """
            Backtracking function to generate happy strings.
            - `index`: Current position in the string.
            - `current_string`: The string formed so far.
            """
            if index == n:
                happy_strings.append(current_string)
                return

            # Determine possible next characters (excluding the last one used)
            next_chars = ["a", "b", "c"]
            next_chars.remove(current_string[-1])

            for next_char in next_chars:
                backtrack(index + 1, current_string + next_char)

        # Start DFS from each possible first character: 'a', 'b', or 'c'
        for start_char in ["a", "b", "c"]:
            backtrack(1, start_char)

        # Return the k-th lexicographically smallest happy string
        return sorted(happy_strings)[k - 1]
