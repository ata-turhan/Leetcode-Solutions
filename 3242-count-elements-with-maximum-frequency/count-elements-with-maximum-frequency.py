class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_value = max(counter.values())
        result = 0

        for value in counter.values():
            if value == max_value:
                result += value

        return result
        