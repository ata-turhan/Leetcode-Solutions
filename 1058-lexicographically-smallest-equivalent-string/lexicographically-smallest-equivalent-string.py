class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        Use Union-Find (Disjoint Set Union) to group equivalent characters.
        Always attach the larger root to the smaller one so that each root 
        represents the lexicographically smallest character in its set.
        """
        # Initialize parent pointers for each lowercase letter
        parent: list[int] = [i for i in range(26)]

        def find(x: int) -> int:
            """
            Find the root of x with path compression.
            """
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            """
            Union the sets containing x and y. Always keep the smaller
            root (lexicographically) as the parent.
            """
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return  # Already in the same set
            # Attach the larger root to the smaller root
            if root_x < root_y:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y

        # Process each pair of equivalent characters
        for ch1, ch2 in zip(s1, s2):
            idx1 = ord(ch1) - ord('a')
            idx2 = ord(ch2) - ord('a')
            union(idx1, idx2)

        # Build the result by mapping each character in baseStr
        # to the lexicographically smallest character in its set
        result_chars: list[str] = []
        for ch in baseStr:
            root_idx = find(ord(ch) - ord('a'))
            smallest_char = chr(root_idx + ord('a'))
            result_chars.append(smallest_char)

        return "".join(result_chars)
