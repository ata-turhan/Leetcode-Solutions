from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split both sentences into words
        words_s1: List[str] = s1.split(" ")
        words_s2: List[str] = s2.split(" ")
        
        # Count the occurrences of each word in both sentences
        count_s1: Counter = Counter(words_s1)
        count_s2: Counter = Counter(words_s2)
        
        # Initialize a list to store the uncommon words
        uncommon_words: List[str] = []

        # Find words that are uncommon in s1 (appear exactly once and not in s2)
        for word in count_s1:
            if count_s1[word] == 1 and word not in count_s2:
                uncommon_words.append(word)

        # Find words that are uncommon in s2 (appear exactly once and not in s1)
        for word in count_s2:
            if count_s2[word] == 1 and word not in count_s1:
                uncommon_words.append(word)

        return uncommon_words
