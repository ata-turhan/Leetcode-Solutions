class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indices = set()

        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(max(0, i - k), min(i + k + 1, len(nums))):
                    if j not in indices:
                        indices.add(j)

        return sorted(list(indices))
        