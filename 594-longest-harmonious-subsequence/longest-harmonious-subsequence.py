class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)

        longest_subsequence = 0

        for num in counter:
            if num + 1 in counter:
                longest_subsequence = max(longest_subsequence, counter[num] + counter.get(num + 1, 0))

        return longest_subsequence
        