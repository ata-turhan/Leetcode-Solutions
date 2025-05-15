class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        start_with_zero = []
        start_with_one = []

        for i, num in enumerate(groups):
            if num == 1:
                if not start_with_one:
                    start_with_one.append(i)
                else:
                    if groups[start_with_one[-1]] == 0:
                        start_with_one.append(i)
                if start_with_zero and groups[start_with_zero[-1]] == 0:
                    start_with_zero.append(i)
            elif num == 0:
                if not start_with_zero:
                    start_with_zero.append(i)
                else:
                    if groups[start_with_zero[-1]] == 1:
                        start_with_zero.append(i)
                if start_with_one and groups[start_with_one[-1]] == 1:
                    start_with_one.append(i)

        res = []
        longest_array = []
        if len(start_with_zero) > len(start_with_one):
            longest_array = start_with_zero
        else:
            longest_array = start_with_one

        for i in longest_array:
            res.append(words[i])

        return res


        