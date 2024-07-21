class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # If k is greater than n, it's impossible to change n to k
        if k > n:
            return -1
        # If n and k are equal, no changes are needed
        elif k == n:
            return 0
        else:
            # Convert n and k to their binary string representations
            n_bin = bin(n)[2:]
            k_bin = bin(k)[2:]
            changes = 0
            
            # Pad k's binary string with leading zeros to match the length of n's binary string
            k_bin = "0" * (len(n_bin) - len(k_bin)) + k_bin

            # Iterate through the binary representations of n and k
            for bit_n, bit_k in zip(n_bin, k_bin):
                # If n has a '1' bit and k has a '0' bit at the same position, increment changes
                if bit_n == "1" and bit_k == "0":
                    changes += 1
                # If n has a '0' bit and k has a '1' bit at the same position, it's impossible to change n to k
                elif bit_n == "0" and bit_k == "1":
                    return -1

            return changes
