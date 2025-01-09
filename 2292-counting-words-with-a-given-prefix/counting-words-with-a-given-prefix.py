class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        """
        Count the number of words that start with a given prefix.

        :param words: List[str] - List of words to search.
        :param pref: str - The prefix to check.
        :return: int - Count of words starting with the prefix.
        """
        # Use a generator expression to check if each word starts with the prefix and sum the results
        return sum(word.startswith(pref) for word in words)
