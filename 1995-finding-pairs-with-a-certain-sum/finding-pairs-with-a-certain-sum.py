from collections import Counter
from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1                  # fixed
        self.nums2 = nums2                  # mutable
        self.freq2 = Counter(nums2)         # frequency map of nums2 for fast lookup

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val
        self.freq2[old_val] -= 1            # decrement count of old value
        if self.freq2[old_val] == 0:
            del self.freq2[old_val]         # clean up zero-count entries

        self.nums2[index] = new_val
        self.freq2[new_val] += 1            # increment count of new value

    def count(self, tot: int) -> int:
        count = 0
        for num in self.nums1:
            complement = tot - num
            count += self.freq2.get(complement, 0)  # lookup in freq map
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)