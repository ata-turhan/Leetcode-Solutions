class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        frequencies = [0] * 3
        count = 0

        for r in range(len(s)):
            char = s[r]
            frequencies[ord(char) - ord("a")] += 1

            while all(frequency > 0 for frequency in frequencies):
                count += len(s) - r
                char = s[l]
                frequencies[ord(char) - ord("a")] -= 1
                l += 1

        return count


        