class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        sorted_idx = {}
        for i, num in enumerate(sorted_arr):
            sorted_idx[num] = i

        chunks = 0
        biggest_idx = -1
        for i, num in enumerate(arr):
            cur_idx = sorted_idx[num]
            biggest_idx = max(biggest_idx, cur_idx)
            if biggest_idx == i:
                chunks += 1

        return chunks
        