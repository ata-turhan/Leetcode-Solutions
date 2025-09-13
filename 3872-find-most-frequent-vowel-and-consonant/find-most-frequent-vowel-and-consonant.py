from typing import List

class Solution:
    def maxFreqSum(self, s: str) -> int:
        """
        Returns the sum of the highest occurring vowel and consonant frequencies in the string.
        Assumes input contains only lowercase English letters.
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_freq = [0] * 26
        consonant_freq = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            if ch in vowels:
                vowel_freq[idx] += 1
            else:
                consonant_freq[idx] += 1

        max_vowel = max(vowel_freq)
        max_consonant = max(consonant_freq)
        return max_vowel + max_consonant
