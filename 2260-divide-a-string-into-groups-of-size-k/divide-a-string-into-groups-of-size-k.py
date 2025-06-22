from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        """
        Divides the string `s` into chunks of size `k`. 
        If the last chunk is shorter than `k`, pads it on the right with `fill` until its length is `k`.

        :param s: The input string to divide.
        :param k: The desired chunk size (must be positive).
        :param fill: The character to use for padding the final chunk if needed.
        :return: A list of equally-sized strings of length `k`.
        """
        if k <= 0:
            raise ValueError("Chunk size k must be a positive integer.")
        
        # Create initial list of chunks
        chunks: List[str] = [s[i : i + k] for i in range(0, len(s), k)]
        
        # If the final chunk is shorter than k, pad it with `fill`
        if chunks and len(chunks[-1]) < k:
            chunks[-1] += fill * (k - len(chunks[-1]))
        
        return chunks
