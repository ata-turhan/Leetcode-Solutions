class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        
        # Build the diff array:
        # diff[i] = 1 if colors[i] != colors[i-1] (with wrap-around for i = 0)
        diff = [0] * n
        diff[0] = 1 if colors[0] != colors[n - 1] else 0
        for i in range(1, n):
            diff[i] = 1 if colors[i] != colors[i - 1] else 0

        # Duplicate diff to handle circular groups
        diff2 = diff + diff

        # Compute prefix sum of diff2 for fast range-sum queries.
        prefix = [0] * (len(diff2) + 1)
        for i in range(len(diff2)):
            prefix[i + 1] = prefix[i] + diff2[i]

        # Count alternating groups.
        count = 0
        # For every starting index in the original circle:
        for i in range(n):
            # The differences to check are from index i+1 to i+k-1 in diff2.
            if prefix[i + k] - prefix[i + 1] == k - 1:
                count += 1

        return count
