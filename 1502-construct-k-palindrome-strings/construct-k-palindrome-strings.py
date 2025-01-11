class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        counter = Counter(s)
        odd_count = sum(value % 2 == 1 for value in counter.values())

        return odd_count <= k
        