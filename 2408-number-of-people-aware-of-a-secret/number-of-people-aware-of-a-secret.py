class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        """
        DP with prefix sums (O(n) time, O(n) space).

        Idea:
        - Let share[d] be the number of people who FIRST learn the secret on day d.
          Those people will start sharing from day (d + delay) and stop (forget) BEFORE day (d + forget).
        - Hence, on day t, the *active sharers* are exactly those who learned on days
          d in [t - forget + 1, t - delay]. They create new learners on day t.
        - We maintain prefix sums over share[] to get window sums in O(1).

        Recurrence:
          share[1] = 1
          For day t >= 2:
             share[t] = sum_{d = t - forget + 1}^{t - delay} share[d]    (if range valid; else 0)

        Answer at the end of day n:
          People who still remember are those who learned on days d in [n - forget + 1, n]
          (i.e., they have known the secret for < forget days).
        """
        MOD = 10**9 + 7

        # share[d] = number of new learners on day d
        share = [0] * (n + 2)
        share[1] = 1

        # prefix[d] = sum_{i=1..d} share[i]  (mod MOD)
        prefix = [0] * (n + 2)
        prefix[1] = 1

        for day in range(2, n + 1):
            # Sharers for 'day' learned in [L, R] = [day - forget + 1, day - delay]
            L = max(1, day - forget + 1)
            R = day - delay

            if R >= L:
                new_learners = (prefix[R] - prefix[L - 1]) % MOD
            else:
                new_learners = 0

            share[day] = new_learners
            prefix[day] = (prefix[day - 1] + share[day]) % MOD

        # Those who still remember at end of day n learned in [n - forget + 1, n]
        L = max(1, n - forget + 1)
        R = n
        return (prefix[R] - prefix[L - 1]) % MOD
