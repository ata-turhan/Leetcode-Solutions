from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        n = len(digits)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    candidate = [digits[i], digits[j], digits[k]]
                    for perm in permutations(candidate):
                        if perm[0] != 0 and perm[2] % 2 == 0:
                            res.append(
                                int("".join(map(str, perm)))
                            )
        
        return list(sorted(set(res)))