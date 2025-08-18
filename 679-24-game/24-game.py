from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def dfs(nums: List[float]) -> bool:
            # If only one number left, check if it's 24 (within tolerance)
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < EPS

            n = len(nums)
            # pick two distinct indices (i < j) to combine
            for i in range(n):
                for j in range(i + 1, n):
                    a, b = nums[i], nums[j]
                    # build list of remaining numbers after removing a and b
                    rest = [nums[k] for k in range(n) if k != i and k != j]

                    # all possible results from combining a and b
                    candidates = [
                        a + b,
                        a * b,
                        a - b,
                        b - a
                    ]
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)

                    # try each candidate and recurse
                    for val in candidates:
                        if dfs(rest + [val]):
                            return True
            return False

        return dfs([float(x) for x in cards])
