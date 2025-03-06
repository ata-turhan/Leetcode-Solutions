class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a_b = [-1, -1]
        n = len(grid)
        possible_nums = set(range(1, n**2 + 1))

        for row in grid:
            for num in row:
                if num not in possible_nums:
                    a_b[0] = num
                else:
                    possible_nums.remove(num)

        b = possible_nums.pop()
        a_b[1] = b
        return a_b
        