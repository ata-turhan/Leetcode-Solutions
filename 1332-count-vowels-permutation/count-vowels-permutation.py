class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize counts for each vowel
        a, e, i, o, u = 1, 1, 1, 1, 1
        
        # Iterate through the length of the string
        for _ in range(1, n):
            # Compute the next counts for each vowel
            a_next = e % MOD
            e_next = (a + i) % MOD
            i_next = (a + e + o + u) % MOD
            o_next = (i + u) % MOD
            u_next = a % MOD
            
            # Update the current counts to the next counts
            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next
        
        # Return the total count of all vowel permutations modulo MOD
        return (a + e + i + o + u) % MOD
