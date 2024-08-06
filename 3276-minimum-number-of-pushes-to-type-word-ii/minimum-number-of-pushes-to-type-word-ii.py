class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_freqs = Counter(word)
        sorted_letters = sorted([(freq, letter) for letter, freq in letter_freqs.items()], reverse=True)
        one_freqs = 0
        two_freqs = 0
        three_freqs = 0
        four_freqs = 0
        letter_moves = defaultdict(int)
        for freq, letter in sorted_letters:
            if one_freqs < 8:
                one_freqs += 1
                letter_moves[letter] = 1
            elif two_freqs < 8:
                two_freqs += 1
                letter_moves[letter] = 2
            elif three_freqs < 8:
                three_freqs += 1
                letter_moves[letter] = 3
            else:
                letter_moves[letter] = 4
        
        moves = 0
        for char in word:
            moves += letter_moves[char]

        return moves
            

        return 0
        