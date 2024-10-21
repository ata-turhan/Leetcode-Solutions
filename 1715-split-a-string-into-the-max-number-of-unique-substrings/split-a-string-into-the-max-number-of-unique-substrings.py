class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def find_max_substrs(index: int, current_substr: str, used_substrs: set) -> int:
            # Base case: if we reach the end of the string
            if index == len(s):
                # If there's a valid current substring left, count it
                return 1 if current_substr and current_substr not in used_substrs else 0

            # Case 1: Continue adding characters to the current substring
            continue_substr = find_max_substrs(index + 1, current_substr + s[index], used_substrs.copy())

            # Case 2: Check if we can start a new substring (if current_substr is valid and not in used_substrs)
            if current_substr and current_substr not in used_substrs:
                used_substrs.add(current_substr)
                start_new_substr = 1 + find_max_substrs(index + 1, s[index], used_substrs)
            else:
                start_new_substr = continue_substr

            # Return the maximum result between continuing or starting a new substring
            return max(continue_substr, start_new_substr)

        return find_max_substrs(0, "", set())
