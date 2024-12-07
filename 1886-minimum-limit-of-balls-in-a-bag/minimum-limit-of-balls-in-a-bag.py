class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def calc_bags(arr, max_size):
            slice_count = 0
            for num in arr:
                slice_count += math.ceil(num / max_size) - 1
            return slice_count

        left = 1
        right = max(nums)
        res = 0
        while left <= right:
            mid = (left + right) // 2
            necessary_count = calc_bags(nums, mid)
            if necessary_count <= maxOperations:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
        