class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = 1
        result = []

        # Calculate products of elements to the left of each element
        for i in range(len(nums)):
            result.append(prefix_product)
            prefix_product *= nums[i]

        # Calculate products of elements to the right of each element
        prefix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= prefix_product
            prefix_product *= nums[i]

        return result

        