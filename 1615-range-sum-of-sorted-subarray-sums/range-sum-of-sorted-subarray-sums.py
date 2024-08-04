class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefix = [0]
        running_sum = 0
        for num in nums:
            running_sum += num
            prefix.append(running_sum)

        sums = []
        for i in range(len(prefix)-1):
            for j in range(i+1, len(prefix)):
                range_sum = prefix[j] - prefix[i]
                sums.append(range_sum)

        sums.sort()

        return sum(sums[left-1:right]) % (10**9 + 7)     