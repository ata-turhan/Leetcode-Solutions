class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = Counter(nums)
        x = max(counter, key=lambda num: counter[num])
        count_x = nums.count(x)
        seen_count_x = 0

        for i, num in enumerate(nums[:-1]):
            if num == x:
                seen_count_x += 1
            if seen_count_x > (i + 1) // 2 and (count_x - seen_count_x) > (len(nums) - i - 1) // 2:
                return i

        return -1
        