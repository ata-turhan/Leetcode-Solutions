class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1_list = sentence1.split(" ")
        s2_list = sentence2.split(" ")
        if len(s1_list) < len(s2_list):
            shorter = s1_list
            longer = s2_list
        else:
            longer = s1_list
            shorter = s2_list
        if shorter == longer[:len(shorter)]:
            return True
        elif shorter == longer[-len(shorter):]:
            return True
        longer_idx = 0
        shorter_idx = 0
        while longer_idx < len(longer):
            if longer[longer_idx] == shorter[shorter_idx]:
                shorter_idx += 1
                longer_idx += 1
            else:
                break
        longer_idx = len(longer) - (len(shorter) - shorter_idx)
        while longer_idx < len(longer):
            if longer[longer_idx] == shorter[shorter_idx]:
                shorter_idx += 1
                longer_idx += 1
            else:
                break
        
        return shorter_idx == len(shorter)


        