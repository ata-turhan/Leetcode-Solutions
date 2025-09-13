class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        vowel_freqs = [0] * 26
        consonant_freqs = [0] * 26

        for letter in s:
            if letter in vowels:
                vowel_freqs[ord(letter) - ord("a")] += 1
            else:
                consonant_freqs[ord(letter) - ord("a")] += 1

        return max(vowel_freqs) + max(consonant_freqs)