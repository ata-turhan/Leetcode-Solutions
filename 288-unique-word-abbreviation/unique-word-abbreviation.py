class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.counts = defaultdict(list)

        for word in dictionary:
            if len(word) < 3:
                self.counts[word].append(word)
            key = word[0] + str(len(word)-2) + word[-1]
            self.counts[key].append(word)
        

    def isUnique(self, word: str) -> bool:
        if len(word) < 3:
            key = word
        else:
            key = word[0] + str(len(word)-2) + word[-1]

        if key not in self.counts:
            return True
        else:
            words = self.counts[key]
            for w in words:
                if w != word:
                    return False
            return True
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)