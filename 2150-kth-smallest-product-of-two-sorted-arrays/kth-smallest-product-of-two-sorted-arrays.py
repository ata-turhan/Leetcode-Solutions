from bisect import bisect_left, bisect_right
import math
from typing import List

class Solution:
    def kthSmallestProduct(
        self,
        nums1: List[int],
        nums2: List[int],
        k: int
    ) -> int:
        """
        Return the k-th smallest product of elements from nums1 and nums2.
        """

        # Helper to count how many pairs have product <= target.
        def count_less_equal(target: int) -> int:
            count: int = 0
            for x in nums1:
                if x > 0:
                    # y must be <= target // x
                    limit = target // x
                    count += bisect_right(nums2, limit)
                elif x < 0:
                    # y must be >= ceil(target / x)
                    threshold = math.ceil(target / x)
                    count += len(nums2) - bisect_left(nums2, threshold)
                else:
                    # x == 0: product is zero
                    if target >= 0:
                        count += len(nums2)
            return count

        # Establish search range from minimal to maximal possible product.
        candidates = [
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1]
        ]
        low: int = min(candidates)
        high: int = max(candidates)

        # Binary search to find the smallest value such that
        # there are at least k products <= that value.
        while low < high:
            mid: int = (low + high) // 2
            if count_less_equal(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low
