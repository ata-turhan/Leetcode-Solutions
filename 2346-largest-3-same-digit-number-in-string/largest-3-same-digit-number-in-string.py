class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """
        Return the lexicographically largest substring of length 3 in `num`
        where all three characters are the same. If none exist, return "".

        Time:  O(n), single pass
        Space: O(1)
        """
        best = ""  # stores the best triple found so far, e.g., "777"

        # Iterate over all length-3 windows
        for i in range(len(num) - 2):
            a, b, c = num[i], num[i + 1], num[i + 2]

            # Check if the window is a "good" integer (all same digit)
            if a == b == c:
                triple = a * 3
                # If we ever find "999" we can return immediately (can't beat it)
                if triple == "999":
                    return triple
                # Update best if this triple is larger
                if triple > best:
                    best = triple

        return best
