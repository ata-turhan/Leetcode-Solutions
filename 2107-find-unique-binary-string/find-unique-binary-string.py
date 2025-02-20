class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i, num in enumerate(nums):
            if num[i] == "0":
                res.append("1")
            else:
                res.append("0")
        return "".join(res)
        