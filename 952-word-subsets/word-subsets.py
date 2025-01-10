class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        combined_letters = defaultdict(int)

        for word in words2:
            letter_counter = Counter(word)
            for key, value in letter_counter.items():
                combined_letters[key] = max(combined_letters[key], value)

        combined_letters = Counter(combined_letters)

        universal_words = []
        for word in words1:
            letter_counter = Counter(word)
            if letter_counter >= combined_letters:
                universal_words.append(word)
        
        return universal_words
        