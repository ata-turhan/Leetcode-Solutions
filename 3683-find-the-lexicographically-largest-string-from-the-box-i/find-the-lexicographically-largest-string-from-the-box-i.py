class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        """
        If numFriends == 1, the only valid piece is the entire string.
        Otherwise, for each starting index i, compute the maximum length L_i
        a piece can have:
          - If i <= (k-1):  L_i = n - (k-1)
          - If i >  (k-1):  L_i = n - i
        Extract word[i : i + L_i] for all i in [0..n-1], pick the lex largest.
        """
        n: int = len(word)
        k: int = numFriends
        
        # Special case: exactly one friend → the only piece must be the whole word.
        if k == 1:
            return word
        
        best: str = ""
        cutoff: int = k - 1
        
        for i in range(n):
            # Determine max length of a piece starting at i
            if i <= cutoff:
                L_i: int = n - cutoff
            else:
                L_i: int = n - i
            
            # Extract that substring
            candidate: str = word[i : i + L_i]
            if candidate > best:
                best = candidate
        
        return best
