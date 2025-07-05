class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky_int = -1

        counter = Counter(arr)

        for key, val in counter.items():
            if key == val:
                lucky_int = max(lucky_int, key)

        return lucky_int
        