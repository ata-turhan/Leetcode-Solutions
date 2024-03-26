from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Count occurrences of each stone
        stone_counts = Counter(stones)
        
        # Sum the counts of stones that are jewels
        return sum(stone_counts[jewel] for jewel in jewels)
