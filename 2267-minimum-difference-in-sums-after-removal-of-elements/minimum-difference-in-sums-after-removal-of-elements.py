from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        Compute the minimum possible (sumFirst - sumSecond) after removing n elements
        from a 3n-length array, where sumFirst is the sum of the first n of the remaining
        elements and sumSecond is the sum of the last n.
        """
        total_len = len(nums)
        n = total_len // 3

        # 1) Build prefix sums of the n smallest values up to each index
        leftMin = [0] * total_len
        max_heap = []          # stores negatives to simulate a max-heap
        prefix_sum = 0

        for i, val in enumerate(nums):
            if len(max_heap) < n:
                # Haven't filled n elements yet -> push directly
                heapq.heappush(max_heap, -val)
                prefix_sum += val
            else:
                # Push new value then pop the largest of the current n+1
                popped_neg = heapq.heappushpop(max_heap, -val)
                # popped_neg is negative of the removed value
                prefix_sum += val + popped_neg   # +popped_neg subtracts the removed original
            leftMin[i] = prefix_sum

        # 2) Build suffix sums of the n largest values from each index to end
        rightMax = [0] * total_len
        min_heap = []          # stores positives for a min-heap
        suffix_sum = 0

        for i in range(total_len - 1, -1, -1):
            val = nums[i]
            if len(min_heap) < n:
                heapq.heappush(min_heap, val)
                suffix_sum += val
            else:
                # Push new value then pop the smallest of the current n+1
                popped = heapq.heappushpop(min_heap, val)
                suffix_sum += val - popped
            rightMax[i] = suffix_sum

        # 3) Evaluate partitions between indices [n-1 .. 2n-1]
        min_diff = float('inf')
        # Partition between k and k+1
        for k in range(n - 1, 2 * n):
            diff = leftMin[k] - rightMax[k + 1]
            if diff < min_diff:
                min_diff = diff

        return min_diff
