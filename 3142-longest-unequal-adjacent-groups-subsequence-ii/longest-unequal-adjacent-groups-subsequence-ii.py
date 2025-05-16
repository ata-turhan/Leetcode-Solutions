from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp: List[int] = [1] * n               # dp[i]: length of longest valid subsequence ending at i
        prev: List[int] = [-1] * n            # prev[i]: predecessor index for reconstruction
        best_end = 0                          # index with maximum dp value

        for i in range(n):
            for j in range(i):
                # ensure group differs and words have same length
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    diffs = 0
                    # compute hamming distance, break early if >1
                    for c1, c2 in zip(words[i], words[j]):
                        if c1 != c2:
                            diffs += 1
                            if diffs > 1:
                                break
                    # update dp and prev when valid transition found
                    if diffs == 1 and dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            # track the overall best end index
            if dp[i] > dp[best_end]:
                best_end = i

        # backtrack to build the subsequence indices
        seq_indices: List[int] = []
        idx = best_end
        while idx != -1:
            seq_indices.append(idx)
            idx = prev[idx]
        seq_indices.reverse()

        # return the words in the reconstructed subsequence
        return [words[k] for k in seq_indices]
