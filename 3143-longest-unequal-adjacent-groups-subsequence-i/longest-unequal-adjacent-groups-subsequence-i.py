from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        Builds the longest subsequence of words such that the group labels alternate between 0 and 1.
        Returns the sequence (not the indices) that forms the longest alternating pattern.
        """
        subseq_starting_with_0 = []
        subseq_starting_with_1 = []

        for i, group in enumerate(groups):
            # Extend subsequence starting with 0
            if not subseq_starting_with_0 or groups[subseq_starting_with_0[-1]] != group:
                subseq_starting_with_0.append(i)

            # Extend subsequence starting with 1
            if not subseq_starting_with_1 or groups[subseq_starting_with_1[-1]] != group:
                subseq_starting_with_1.append(i)

        # Choose the longer alternating subsequence
        longest_indices = (
            subseq_starting_with_0 if len(subseq_starting_with_0) >= len(subseq_starting_with_1)
            else subseq_starting_with_1
        )

        return [words[i] for i in longest_indices]
