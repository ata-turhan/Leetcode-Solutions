class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        
        num_operations = 0

        while len(nums) >= 2:
            if nums[0] >= k:
                break
                
            x, y = heappop(nums), heappop(nums)
            heappush(nums, min(x, y) * 2 + max(x, y))
            num_operations += 1

            

        return num_operations
        