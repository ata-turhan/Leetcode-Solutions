class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        neg_gifts = [-gift for gift in gifts]
        heapify(neg_gifts)
        for _ in range(k):
            max_gift_count = -1 * heappop(neg_gifts)
            new_gift_count = math.floor(max_gift_count**0.5)
            heappush(neg_gifts, -1 * new_gift_count)

        return -1 * sum(neg_gifts)
