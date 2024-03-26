class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        list1_map = {}
        for i, word in enumerate(list1):
            list1_map[word] = i
        min_sum = float("inf")
        for j, word in enumerate(list2):
            if word in list1_map:
                i = list1_map[word]
                if i + j < min_sum:
                    res = [word]
                    min_sum = i + j
                elif i + j == min_sum:
                    res.append(word)
        return res
        