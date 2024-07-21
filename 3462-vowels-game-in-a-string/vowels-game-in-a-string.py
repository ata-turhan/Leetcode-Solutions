class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # Initialize the vowel count to zero
        vowel_count = 0
        
        # Iterate through each character in the string
        for char in s:
            # Check if the character is a vowel
            if char in "aeiou":
                # Increment the vowel count
                vowel_count += 1

        # If there are no vowels, Alice loses
        if vowel_count == 0:
            return False
        else:
            # If there is at least one vowel, Alice wins
            return True
