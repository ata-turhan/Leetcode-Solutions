class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_idx = -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                if mid == len(nums) - 1:
                    neg_idx = len(nums)
                    break
                else:
                    left = mid + 1
            else:
                if nums[mid] >= 0:
                    if mid == 0:
                        neg_idx = 0
                        break
                    else:
                        right = mid - 1
                        neg_idx = mid

        pos_idx = -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= 0:
                if mid == len(nums) - 1:
                    pos_idx = len(nums)
                    break
                else:
                    left = mid + 1
            else:
                if nums[mid] > 0:
                    if mid == 0:
                        pos_idx = 0
                        break
                    else:
                        right = mid - 1
                        pos_idx = mid

        neg_count = neg_idx
        pos_count = len(nums) - pos_idx


        return max(neg_count, pos_count)