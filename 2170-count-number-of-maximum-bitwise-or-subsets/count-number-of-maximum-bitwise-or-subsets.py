class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_val = reduce(lambda a, b: a | b, nums)
        
        def find_max_subsets(i, current_or):
            if i == len(nums):
                return 1 if current_or == max_or_val else 0

            option1 = find_max_subsets(i+1, current_or | nums[i])
            option2 = find_max_subsets(i+1, current_or)

            return option1 + option2

        return find_max_subsets(0, 0)
        