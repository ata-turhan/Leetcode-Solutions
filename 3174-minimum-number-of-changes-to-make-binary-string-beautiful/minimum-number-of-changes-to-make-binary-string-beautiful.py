class Solution:
    def minChanges(self, s: str) -> int:
        cons_counts = []
        prev_char = ""
        char_count = 0
        
        for char in s:
            if char == prev_char:
                char_count += 1
            else:
                if char_count != 0:
                    cons_counts.append(char_count)
                prev_char = char
                char_count = 1
        cons_counts.append(char_count)

        change_count = 0
        for i in range(len(cons_counts)):
            if cons_counts[i] % 2 != 0:
                change_count += 1
                if i < len(cons_counts) - 1:
                    cons_counts[i+1] += 1

        return change_count
                
        