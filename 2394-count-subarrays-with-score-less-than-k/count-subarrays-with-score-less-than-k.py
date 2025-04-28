class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        subarray_count = 0
        cur_sum = 0

        for r in range(len(nums)):
            cur_sum += nums[r]

            while l <= r and cur_sum * (r - l + 1) >= k:
                cur_sum -= nums[l]
                l += 1

            if l <= r:
                subarray_count += (r - l + 1)

        return subarray_count
        