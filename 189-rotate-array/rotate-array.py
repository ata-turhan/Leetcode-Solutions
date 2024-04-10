class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)  # Calculate the actual rotation amount within the length of nums
        nums.reverse()  # Reverse the entire list
        nums[:k] = reversed(nums[:k])  # Reverse the first k elements
        nums[k:] = reversed(nums[k:])  # Reverse the remaining elements

        """
        # Alternative method using pop and insert
        for i in range(k):
            a = nums.pop()
            nums.insert(0, a)
        """
