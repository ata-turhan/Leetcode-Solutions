import math

class SegmentTree:
    """A segment tree for range minimum queries and point updates."""
    def __init__(self, size):
        self.size = size
        self.tree = [math.inf] * (2 * size)

    def update(self, index, value):
        """Sets the value at a specific index, updating the tree."""
        pos = index + self.size
        # We only update if the new value is smaller
        if value < self.tree[pos]:
            self.tree[pos] = value
            while pos > 1:
                pos //= 2
                self.tree[pos] = min(self.tree[pos * 2], self.tree[pos * 2 + 1])

    def query(self, left, right):
        """Queries the minimum value in the range [left, right)."""
        if left >= right:
            return math.inf
        res = math.inf
        l = left + self.size
        r = right + self.size
        while l < r:
            if l % 2:
                res = min(res, self.tree[l])
                l += 1
            if r % 2:
                r -= 1
                res = min(res, self.tree[r])
            l //= 2
            r //= 2
        return res

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        chars = ['0', '1', '2', '3', '4']
        global_max_diff = -math.inf

        for a in chars:
            for b in chars:
                if a == b:
                    continue

                prefix_a = [0] * (n + 1)
                prefix_b = [0] * (n + 1)
                for i in range(n):
                    prefix_a[i + 1] = prefix_a[i] + (1 if s[i] == a else 0)
                    prefix_b[i + 1] = prefix_b[i] + (1 if s[i] == b else 0)

                sts = [[SegmentTree(n + 2) for _ in range(2)] for _ in range(2)]

                # Initial state for i=0 (empty prefix)
                val_0 = prefix_a[0] - prefix_b[0]
                pa_0 = prefix_a[0] % 2
                pb_0 = prefix_b[0] % 2
                cb_0 = prefix_b[0]
                sts[pa_0][pb_0].update(cb_0, val_0)
                
                # We start the main loop from j=k because substrings must have length at least k
                for j in range(k, n + 1):
                    # Add prefix info for i = j - k into the data structure.
                    # This i is now available for substrings ending at j or later.
                    i = j - k
                    val_i = prefix_a[i] - prefix_b[i]
                    pa_i = prefix_a[i] % 2
                    pb_i = prefix_b[i] % 2
                    cb_i = prefix_b[i]
                    sts[pa_i][pb_i].update(cb_i, val_i)
                    
                    # Find the best i for the current j.
                    val_j = prefix_a[j] - prefix_b[j]
                    pa_j = prefix_a[j] % 2
                    pb_j = prefix_b[j] % 2
                    cb_j = prefix_b[j]
                    
                    target_pa = 1 - pa_j
                    target_pb = pb_j

                    min_val_i = sts[target_pa][target_pb].query(0, cb_j)

                    if min_val_i != math.inf:
                        global_max_diff = max(global_max_diff, val_j - min_val_i)
        
        # The problem statement guarantees a valid substring exists, so global_max_diff will be updated.
        # Example 1 output is -1, so negative results are valid.
        return global_max_diff if global_max_diff != -math.inf else -1