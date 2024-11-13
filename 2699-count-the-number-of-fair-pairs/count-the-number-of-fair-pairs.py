class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        num_pairs = 0
        print(nums)

        for i, num in enumerate(nums):
            smallest_pair_idx = bisect.bisect_left(nums, lower - num)
            largest_pair_idx  = bisect.bisect_right(nums, upper - num)
            if smallest_pair_idx == len(nums):
                continue
            if largest_pair_idx == 0:
                continue
            largest_pair_idx -= 1
            smallest_pair_idx = max(smallest_pair_idx, i + 1)
            largest_pair_idx = max(largest_pair_idx, i + 1)
            if largest_pair_idx >= smallest_pair_idx and smallest_pair_idx < len(nums) and largest_pair_idx < len(nums) and num + nums[smallest_pair_idx] >= lower and num + nums[largest_pair_idx] <= upper:
                num_pairs += (largest_pair_idx - smallest_pair_idx + 1)
                print(num, smallest_pair_idx, largest_pair_idx)

        return num_pairs
        