class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        chars = list(s)
        res = []
        space_idx = len(spaces) - 1
        for i in range(len(chars) - 1, -1, -1):
            res.append(chars[i])
            if i == spaces[space_idx]:
                res.append(" ")
                space_idx -= 1

        return "".join(reversed(res))
        