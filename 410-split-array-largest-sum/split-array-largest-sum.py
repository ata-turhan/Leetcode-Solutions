class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def split(max_val, m):
            cur_sum = 0
            k = 1
            for num in nums:
                if cur_sum + num <= max_val:
                    cur_sum += num
                else:
                    cur_sum = num
                    k += 1
                    if k > m:
                        return float("inf")
            return k
                    

        left = max(nums)
        right = sum(nums)
        min_sum = float("inf")
        while left <= right:
            mid = left + (right - left) // 2
            subarray_count = split(mid, m)
            if subarray_count <= m:
                right = mid - 1
                min_sum = min(min_sum, mid)
            else:
                left = mid + 1
        return min_sum