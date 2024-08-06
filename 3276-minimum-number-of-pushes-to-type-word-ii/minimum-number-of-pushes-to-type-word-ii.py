from collections import Counter, defaultdict

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the frequency of each letter in the word
        letter_frequencies = Counter(word)
        
        # Sort letters by their frequency in descending order
        sorted_letters = sorted([(freq, letter) for letter, freq in letter_frequencies.items()], reverse=True)
        
        # Initialize counters for letters with different push costs
        cost_1_count = 0
        cost_2_count = 0
        cost_3_count = 0
        
        # Dictionary to map each letter to its push cost
        letter_push_costs = defaultdict(int)
        
        # Assign push costs based on frequency rank
        for freq, letter in sorted_letters:
            if cost_1_count < 8:
                cost_1_count += 1
                letter_push_costs[letter] = 1
            elif cost_2_count < 8:
                cost_2_count += 1
                letter_push_costs[letter] = 2
            elif cost_3_count < 8:
                cost_3_count += 1
                letter_push_costs[letter] = 3
            else:
                letter_push_costs[letter] = 4
        
        # Calculate the total number of moves needed to type the word
        total_moves = 0
        for char in word:
            total_moves += letter_push_costs[char]
        
        return total_moves
