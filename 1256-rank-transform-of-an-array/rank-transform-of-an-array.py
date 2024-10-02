class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        sorted_arr = sorted(list(set(arr)))
        ranks = {}
        for rank, num in enumerate(sorted_arr, start=1):
            ranks[num] = rank
        res = []
        for num in arr:
            res.append(ranks[num])
        return res

        