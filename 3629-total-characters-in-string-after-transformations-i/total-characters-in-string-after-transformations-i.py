class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        """
        Compute the length of the string after t transformations,
        where 'a'->'b', ..., 'y'->'z', 'z'->"ab", modulo 10^9+7.
        """
        MOD: int = 10**9 + 7

        # 1. Initialize frequency vector for 'a'..'z'
        cnt: list[int] = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # 2. Apply t transformations on the frequency vector
        for _ in range(t):
            new_cnt: list[int] = [0] * 26

            # Shift counts for 'a'..'y' to the next letter
            for i in range(25):
                new_cnt[i + 1] = cnt[i]

            # Handle 'z' -> "ab"
            zc: int = cnt[25]
            new_cnt[0] = (new_cnt[0] + zc) % MOD  # add to 'a'
            new_cnt[1] = (new_cnt[1] + zc) % MOD  # add to 'b'

            # Take modulo for all entries to prevent overflow
            for i in range(26):
                new_cnt[i] %= MOD

            cnt = new_cnt

        # 3. Sum all frequencies to get total length
        return sum(cnt) % MOD
