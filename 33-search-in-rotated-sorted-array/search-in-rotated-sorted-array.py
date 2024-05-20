class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[start] <= nums[mid]:
                # Target is in the left sorted half
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # Right half is sorted
            else:
                # Target is in the right sorted half
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1
