class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_arr = s1.split(" ")
        s2_arr = s2.split(" ")
        s1_words = Counter(s1_arr)
        s2_words = Counter(s2_arr)
        uncommon_words = []

        for word in s1_words:
            if s1_words[word] == 1 and word not in s2_words:
                uncommon_words.append(word)

        for word in s2_words:
            if s2_words[word] == 1 and word not in s1_words:
                uncommon_words.append(word)

        return uncommon_words