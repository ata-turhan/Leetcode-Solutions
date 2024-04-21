from collections import defaultdict
from itertools import combinations
from math import lcm

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        # Store combinations of coins and their least common multiple
        combinations_lcm = defaultdict(list)
        for i in range(1, n + 1):
            for comb in combinations(coins, i):
                combinations_lcm[len(comb)].append(lcm(*comb))
        
        # Function to count the number of multiples of least common multiples less than or equal to target
        def count_multiples(dic, target):
            ans = 0
            for i in range(1, n + 1):
                for lcm_val in dic[i]:
                    ans += target // lcm_val * pow(-1, i + 1)
            return ans
        
        # Binary search to find the kth smallest number
        start, end = min(coins), min(coins) * k
        while start + 1 < end:
            mid = (start + end) // 2
            if count_multiples(combinations_lcm, mid) >= k:
                end = mid
            else:
                start = mid
        if count_multiples(combinations_lcm, start) >= k:
            return start
        else:
            return end
