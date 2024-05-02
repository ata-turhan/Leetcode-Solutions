import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[]]  # Return empty list if input is empty
        grouped_anagrams = collections.defaultdict(list)
        for word in strs:
            if len(word) == 0:
                grouped_anagrams[""].append("")  # Handle empty string case
            else:
                sorted_word = "".join(sorted(word))
                grouped_anagrams[sorted_word].append(word)
        return list(grouped_anagrams.values())  # Convert to list for the expected output format
