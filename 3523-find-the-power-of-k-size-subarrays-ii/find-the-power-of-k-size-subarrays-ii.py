class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        stack = deque([0])
        for i in range(1, k-1):
            while stack and nums[stack[-1]] != (nums[i] - 1):
                stack.pop()
            stack.append(i)

        for i in range(k-1, len(nums)):
            while stack and nums[stack[-1]] != (nums[i] - 1):
                stack.pop()
            stack.append(i)
            if len(stack) == k:
                res.append(nums[stack[-1]])
            else:
                res.append(-1)
            if stack[0] == (i - k + 1): 
                stack.popleft()

        return res

        