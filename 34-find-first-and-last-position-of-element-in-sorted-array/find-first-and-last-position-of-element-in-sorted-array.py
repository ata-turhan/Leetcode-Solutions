class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Function to find the starting index of target
        def find_start(nums, target):
            start = -1
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    # If mid is the first occurrence of target or the previous element is not target
                    if mid == 0 or nums[mid] != nums[mid - 1]:
                        start = mid
                        break
                    else:
                        # Continue search in the left half
                        right = mid - 1
                elif nums[mid] < target:
                    # Move to the right half
                    left = mid + 1
                else:
                    # Move to the left half
                    right = mid - 1
            return start
        
        # Function to find the ending index of target
        def find_end(nums, target):
            end = -1
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    # If mid is the last occurrence of target or the next element is not target
                    if mid == len(nums) - 1 or nums[mid] != nums[mid + 1]:
                        end = mid
                        break
                    else:
                        # Continue search in the right half
                        left = mid + 1
                elif nums[mid] < target:
                    # Move to the right half
                    left = mid + 1
                else:
                    # Move to the left half
                    right = mid - 1
            return end

        # Find the starting and ending indices of target
        start = find_start(nums, target)
        end = find_end(nums, target)
        
        return [start, end]
