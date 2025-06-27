from typing import List, Dict

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        """
        Finds the longest subsequence that can be repeated k times in s.
        If multiple have the same max length, returns the lexicographically largest.
        """
        n: int = len(s)
        # 1) Frequency count
        freq: Dict[str, int] = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # 2) Characters usable in the subsequence and their max counts
        max_counts: Dict[str, int] = {
            ch: freq[ch] // k for ch in freq if freq[ch] >= k
        }
        if not max_counts:
            return ""

        # Sort chars in descending lex order to find lex-largest candidates first
        candidates: List[str] = sorted(max_counts.keys(), reverse=True)
        total_allowed: int = sum(max_counts.values())

        # 3) Build next-position table: next_pos[i][c] = first index ≥ i where s[index]==c, else n
        # Size is (n+1) × 26
        next_pos: List[List[int]] = [[n] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            # Copy forward
            next_pos[i] = next_pos[i + 1].copy()
            # Update for s[i]
            next_pos[i][ord(s[i]) - ord('a')] = i

        # Helper to check if seq repeated k times is a subsequence of s
        def can_repeat(seq: List[str]) -> bool:
            idx = 0
            for _ in range(k):
                for ch in seq:
                    nxt = next_pos[idx][ord(ch) - ord('a')]
                    if nxt == n:
                        return False
                    idx = nxt + 1
            return True

        best_seq: List[str] = []
        best_length: int = 0

        # Track usage counts of each candidate char
        used_counts: Dict[str, int] = {ch: 0 for ch in candidates}

        def dfs(cur_seq: List[str]) -> None:
            nonlocal best_seq, best_length
            # Prune if even using all remaining capacity can't beat best_length
            if len(cur_seq) + (total_allowed - len(cur_seq)) <= best_length:
                return

            for ch in candidates:
                if used_counts[ch] < max_counts[ch]:
                    # Try appending ch
                    cur_seq.append(ch)
                    used_counts[ch] += 1

                    if can_repeat(cur_seq):
                        # Update best if longer or same length but lex larger
                        if (len(cur_seq) > best_length or
                            (len(cur_seq) == best_length and cur_seq > best_seq)):
                            best_seq = cur_seq.copy()
                            best_length = len(cur_seq)
                        # Recurse deeper
                        dfs(cur_seq)

                    # Backtrack
                    used_counts[ch] -= 1
                    cur_seq.pop()

        # Launch DFS from empty sequence
        dfs([])

        return "".join(best_seq)
