class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """
        Applies a series of shifts to the string `s` based on the operations in `shifts`.

        :param s: The input string consisting of lowercase letters.
        :param shifts: List of shift operations [start, end, direction].
                       - start: Starting index of the range to apply the shift.
                       - end: Ending index of the range to apply the shift.
                       - direction: 0 for left shift, 1 for right shift.
        :return: The modified string after applying all shifts.
        """
        def shift_character(character: str, shift: int) -> str:
            """
            Shifts a character by `shift` positions in the alphabet, wrapping around as necessary.
            """
            return chr(ord('a') + (ord(character) - ord('a') + shift) % 26)

        # Array to calculate cumulative shift impacts on each character
        shift_effects = [0] * len(s)

        # Apply shift effects for each operation
        for start, end, direction in shifts:
            shift_effects[start] += -1 if direction == 0 else 1
            if end + 1 < len(shift_effects):
                shift_effects[end + 1] += 1 if direction == 0 else -1

        # Compute the prefix sum of shifts to determine final shift for each character
        for i in range(1, len(shift_effects)):
            shift_effects[i] += shift_effects[i - 1]

        # Apply the computed shifts to the string
        result_chars = list(s)
        for i in range(len(result_chars)):
            result_chars[i] = shift_character(result_chars[i], shift_effects[i])

        # Join the result characters into the final string
        return "".join(result_chars)
