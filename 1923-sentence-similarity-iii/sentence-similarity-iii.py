class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split the sentences into words
        words1 = sentence1.split(" ")
        words2 = sentence2.split(" ")

        # Ensure that words1 refers to the longer sentence
        if len(words1) < len(words2):
            shorter_sentence, longer_sentence = words1, words2
        else:
            longer_sentence, shorter_sentence = words1, words2

        # Check if the shorter sentence matches the start of the longer sentence
        if shorter_sentence == longer_sentence[:len(shorter_sentence)]:
            return True

        # Check if the shorter sentence matches the end of the longer sentence
        elif shorter_sentence == longer_sentence[-len(shorter_sentence):]:
            return True

        # Now, check for matches in the middle of the longer sentence
        longer_index = 0
        shorter_index = 0

        # Try to match the words from the beginning
        while longer_index < len(longer_sentence):
            if longer_sentence[longer_index] == shorter_sentence[shorter_index]:
                shorter_index += 1
                longer_index += 1
            else:
                break

        # Adjust the index to match words from the end
        longer_index = len(longer_sentence) - (len(shorter_sentence) - shorter_index)
        while longer_index < len(longer_sentence):
            if longer_sentence[longer_index] == shorter_sentence[shorter_index]:
                shorter_index += 1
                longer_index += 1
            else:
                break

        # If all words of the shorter sentence were matched, return True
        return shorter_index == len(shorter_sentence)
