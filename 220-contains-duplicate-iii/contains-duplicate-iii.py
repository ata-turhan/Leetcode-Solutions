from sortedcontainers import SortedSet

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        set_nums = SortedSet()
        for i in range(len(nums)):
            # Find the successor of current element
            s = set_nums.bisect_left(nums[i])
            if s < len(set_nums) and abs(set_nums[s] - nums[i]) <= t:
                return True

            # Find the predecessor of current element
            g = set_nums.bisect_left(nums[i] - t)
            if g < len(set_nums) and abs(nums[i] - set_nums[g]) <= t:
                return True

            set_nums.add(nums[i])
            if len(set_nums) > k:
                set_nums.remove(nums[i - k])

        return False
