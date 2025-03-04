from math import log

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        @cache
        def is_sum(num):
            if num == 0:
                return True
            elif num < 0:
                return False

            base = int(log(n, 3))
            for i in range(base, -1, -1):
                if i in used_powers:
                    continue
                used_powers.add(i)
                if is_sum(num - 3 ** i):
                    return True
                used_powers.remove(i)

            return False

        used_powers = set()

        return is_sum(n)

        