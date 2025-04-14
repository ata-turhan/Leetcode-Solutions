from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        Counts the number of good triplets (i, j, k) such that:
        0 <= i < j < k < len(arr) and
        |arr[i] - arr[j]| <= a,
        |arr[j] - arr[k]| <= b,
        |arr[i] - arr[k]| <= c
        """
        n = len(arr)
        good_triplet_count = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        good_triplet_count += 1

        return good_triplet_count
