class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        nums_indices = [(num, i) for i, num in enumerate(nums)]
        heapify(nums_indices)
        score = 0

        while nums_indices:
            num, i = heappop(nums_indices)
            if i not in marked:
                score += num
                marked.add(i-1)
                marked.add(i+1)

        return score
        