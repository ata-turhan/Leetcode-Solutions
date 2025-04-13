class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        # Calculate the number of even-indexed positions (0-indexed)
        even_positions = (n + 1) // 2
        # Calculate the number of odd-indexed positions (0-indexed)
        odd_positions = n // 2
        
        # Compute the result using modular exponentiation:
        # 5 choices for even indices and 4 choices for odd indices.
        result = (pow(5, even_positions, mod) * pow(4, odd_positions, mod)) % mod
        return result
