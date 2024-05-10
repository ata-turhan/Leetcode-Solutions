class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []

        for i in range(len(arr)-1):
            heapq.heappush(heap, (arr[i]/arr[len(arr)-1], i, len(arr)-1))

        for _ in range(k-1):
            smallest_frac, nominator, denominator = heapq.heappop(heap)
            if nominator < denominator - 1:
                heapq.heappush(heap, (arr[nominator]/arr[denominator-1], nominator, denominator-1))

        kth_smallest_frac, kth_smallest_nominator, kth_smallest_denominator = heapq.heappop(heap)
        return [arr[kth_smallest_nominator], arr[kth_smallest_denominator]]
        