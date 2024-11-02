class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Split the sentence into words
        words = sentence.split()
        
        # Check if the last letter of the last word matches the first letter of the first word
        if words[-1][-1] != words[0][0]:
            return False

        # Check that each word begins with the last letter of the previous word
        for i in range(1, len(words)):
            if words[i][0] != words[i - 1][-1]:
                return False

        # If all checks pass, return True
        return True
