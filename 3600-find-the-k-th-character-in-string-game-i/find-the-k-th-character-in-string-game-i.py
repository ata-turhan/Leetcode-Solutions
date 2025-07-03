class Solution:
    def kthCharacter(self, k: int) -> str:
        def convert_word(arr):
            new_arr = []
            for char in arr:
                new_char =  chr((ord(char) - ord("a") + 1) % 26 + ord("a"))
                new_arr.append(new_char)
            return arr + new_arr


        word = ["a"]

        while len(word) < k:
            word = convert_word(word)

        return word[k - 1]