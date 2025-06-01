class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        Return the number of ordered triples (x, y, z) of nonnegative integers
        such that x + y + z = n and 0 <= x, y, z <= limit.
        """

        # 1) If limit >= n, there is no upper‐cap restriction in practice.
        #    Number of nonnegative solutions to x+y+z = n is C(n+2, 2).
        if limit >= n:
            return (n + 1) * (n + 2) // 2

        # 2) If n > 3*limit, even giving each child 'limit' candies yields < n total.
        if n > 3 * limit:
            return 0

        # 3) Now we are in the range: limit < n <= 3*limit.
        #    Define P = n - limit.  Then we will sum i from 0..limit,
        #    splitting into two sub‐ranges depending on whether i <= P or i > P.
        P = n - limit

        # The smallest i at which f(i)=2*limit - n + i + 1 becomes positive is
        # i0 = max(0, n - 2*limit).  Below i0, f(i) <= 0, so no contribution.
        i0 = max(0, n - 2 * limit)

        total = 0

        # CASE A: If P >= limit, all valid i in [i0..limit] use f(i).
        #         No "Region B" needed in that case.
        if P >= limit:
            # Sum_{i = i0..limit} [ 2*limit - n + i + 1 ]
            # Let countA = (limit - i0 + 1)
            countA = limit - i0 + 1

            # Sum_i from i0..limit of i = (limit*(limit+1)//2) - ( (i0-1)*i0 // 2 )
            sum_i_to_limit = limit * (limit + 1) // 2
            sum_i_before_i0 = (i0 - 1) * i0 // 2 if i0 > 0 else 0
            range_sum_i = sum_i_to_limit - sum_i_before_i0

            # Constant term = (2*limit - n + 1)
            const_term = 2 * limit - n + 1

            total = range_sum_i + const_term * countA

        else:
            # We have two regions: RegionA: i in [i0..P], RegionB: i in [P+1..limit].

            # === Region A: i = i0..P, contribution = f(i) = 2*limit - n + i + 1 ===
            if i0 <= P:
                countA = P - i0 + 1

                sum_i_to_P = P * (P + 1) // 2
                sum_i_before_i0 = (i0 - 1) * i0 // 2 if i0 > 0 else 0
                regionA_sum_i = sum_i_to_P - sum_i_before_i0

                constA = 2 * limit - n + 1
                total += regionA_sum_i + constA * countA

            # === Region B: i = P+1..limit, contribution = g(i) = n - i + 1 ===
            # Since P < limit, Region B exists.
            lowB = P + 1
            highB = limit
            countB = highB - lowB + 1

            # Sum_{i = lowB..highB} of (n - i + 1) 
            #   = (n + 1) * countB - sum_{i=lowB..highB} i
            sum_i_to_highB = highB * (highB + 1) // 2
            sum_i_before_lowB = (lowB - 1) * lowB // 2
            sum_i_lowB_to_highB = sum_i_to_highB - sum_i_before_lowB

            total += (n + 1) * countB - sum_i_lowB_to_highB

        return total
