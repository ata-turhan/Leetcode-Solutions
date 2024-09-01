class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        res = []
        for i in range(0, len(original), n):
            res.append(original[i:i+n])

        return res