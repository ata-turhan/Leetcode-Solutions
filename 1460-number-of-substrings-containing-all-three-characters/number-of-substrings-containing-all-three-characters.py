class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """Counts the number of substrings containing at least one of each character 'a', 'b', and 'c'."""
        
        left_pointer = 0
        char_frequencies = [0] * 3
        substring_count = 0

        for right_pointer in range(len(s)):
            char_frequencies[ord(s[right_pointer]) - ord("a")] += 1

            while all(freq > 0 for freq in char_frequencies):
                substring_count += len(s) - right_pointer
                char_frequencies[ord(s[left_pointer]) - ord("a")] -= 1
                left_pointer += 1

        return substring_count
