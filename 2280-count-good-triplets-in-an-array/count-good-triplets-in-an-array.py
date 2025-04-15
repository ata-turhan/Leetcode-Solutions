from typing import List

class FenwickTree:
    def __init__(self, size: int):
        self.tree = [0] * (size + 2)
        self.size = size + 2

    def update(self, index: int, value: int) -> None:
        index += 1  # 1-based indexing
        while index < self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index: int) -> int:
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n: int = len(nums1)
        pos_in_nums2: List[int] = [0] * n
        for i, val in enumerate(nums2):
            pos_in_nums2[val] = i

        # Transform nums1 into the order of positions in nums2
        nums1_mapped: List[int] = [pos_in_nums2[val] for val in nums1]

        # Count of good triplets centered at each index
        left_tree = FenwickTree(n)
        left_smaller: List[int] = [0] * n

        for i in range(n):
            left_smaller[i] = left_tree.query(nums1_mapped[i] - 1)
            left_tree.update(nums1_mapped[i], 1)

        right_tree = FenwickTree(n)
        right_larger: List[int] = [0] * n

        for i in range(n - 1, -1, -1):
            right_larger[i] = right_tree.query(n - 1) - right_tree.query(nums1_mapped[i])
            right_tree.update(nums1_mapped[i], 1)

        total_good_triplets: int = 0
        for i in range(n):
            total_good_triplets += left_smaller[i] * right_larger[i]

        return total_good_triplets
