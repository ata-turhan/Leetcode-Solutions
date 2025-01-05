class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        def change_letter(letter, shift):
            return chr(ord("a") + (ord(letter) - ord("a") + shift) % 26)

        shift_amounts = [0] * len(s)
        for start, end, direction in shifts:
            shift_amounts[start] += -1 if direction == 0 else 1
            if end != len(shift_amounts) - 1:
                shift_amounts[end + 1] += 1 if direction == 0 else -1

        for i in range(1, len(shift_amounts)):
            shift_amounts[i] += shift_amounts[i-1]

        arr_string = list(s)
        for i in range(len(arr_string)):
            arr_string[i] = change_letter(arr_string[i], shift_amounts[i])

        return "".join(arr_string)

        
        