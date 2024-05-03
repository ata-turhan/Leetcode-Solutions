class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        i, j = 0, 0
        while i < len(v1) or j < len(v2):
            if i >= len(v1):
                el1 = 0
            else:
                el1 = v1[i]
            if j >= len(v2):
                el2 = 0
            else:
                el2 = v2[j]
            if el1 < el2:
                return -1
            elif el1 > el2:
                return 1
            else:
                i += 1
                j += 1
        return 0