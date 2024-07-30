class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        
        # Compute prefix sums of `b` counts
        prefix_b = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_b[i] = prefix_b[i - 1] + (s[i - 1] == 'b')

        # Compute suffix sums of `a` counts
        suffix_a = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_a[i] = suffix_a[i + 1] + (s[i] == 'a')

        # Calculate minimum deletions required
        min_deletions = float('inf')
        for i in range(n + 1):
            deletions = prefix_b[i] + suffix_a[i]
            min_deletions = min(min_deletions, deletions)

        return min_deletions
