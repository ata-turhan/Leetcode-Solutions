class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l = 0
        subarray_count = 0
        count_distincts = len(set(nums))
        subarray_dict = defaultdict(int) 

        for r in range(len(nums)):
            subarray_dict[nums[r]] += 1

            while l <= r and len(subarray_dict) == count_distincts:
                subarray_count += len(nums) - r
                subarray_dict[nums[l]] -= 1
                if subarray_dict[nums[l]] == 0:
                    subarray_dict.pop(nums[l])
                l += 1

        return subarray_count
        