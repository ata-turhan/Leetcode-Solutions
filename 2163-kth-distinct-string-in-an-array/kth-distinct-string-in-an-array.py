class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freqs = defaultdict(int)
        for word in arr:
            freqs[word] += 1

        dist_count = 0
        for word in arr:
            if freqs[word] == 1:
                dist_count += 1
            if dist_count == k:
                return word
                
        return ""