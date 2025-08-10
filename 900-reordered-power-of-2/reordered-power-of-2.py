class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Helper: returns sorted string of digits for a number
        def signature(x: int) -> str:
            return ''.join(sorted(str(x)))
        
        # Precompute signatures of all powers of two up to 10^9
        power_signatures = {signature(1 << k) for k in range(31)}  # 2^0 .. 2^30
        
        # Check if n's signature matches any precomputed power-of-two signature
        return signature(n) in power_signatures
