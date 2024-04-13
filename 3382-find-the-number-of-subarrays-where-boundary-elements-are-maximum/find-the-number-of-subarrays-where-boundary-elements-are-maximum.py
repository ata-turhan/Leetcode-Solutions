from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        stack = []
        subarrays_count = len(nums)
        element_count = defaultdict(int)
        
        # Non-increasing stack
        for num in nums:
            while stack and num > stack[-1]:
                prev_element = stack.pop()
                element_count[prev_element] = 0
                
            if stack and num == stack[-1]:
                element_count[num] += 1
                subarrays_count += element_count[num]
                
            stack.append(num)
        
        return subarrays_count
