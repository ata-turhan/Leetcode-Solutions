class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = [-h for h in happiness]
        heapq.heapify(happiness)
        
        res = 0
        for count in range(1, k+1):
            happiness_val = -heapq.heappop(happiness)
            res += max(0, happiness_val - count + 1)
        return res
        