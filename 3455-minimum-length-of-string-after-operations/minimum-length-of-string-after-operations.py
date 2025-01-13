class Solution:
    def minimumLength(self, s: str) -> int:
        letter_counts = Counter(s)
        for key, value in letter_counts.items():
            if value % 2 == 1:
                letter_counts[key] = 1
            elif value % 2 == 0:
                letter_counts[key] = 2

        return sum(value for value in letter_counts.values())
        