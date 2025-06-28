class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        largest_sum_list = Counter(sorted(nums)[-k:])

        res = []

        for num in nums:
            if num in largest_sum_list:
                res.append(num)
                largest_sum_list[num] -= 1
                if largest_sum_list[num] == 0:
                    largest_sum_list.pop(num)

        return res
                
        