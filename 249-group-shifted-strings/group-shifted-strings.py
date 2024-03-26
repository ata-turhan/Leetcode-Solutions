class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strings:
            key = ""
            shift = ord(string[0]) - ord("a")
            for i in range(len(string)):
                new_ord = ord(string[i]) - shift
                if new_ord < 97:
                    new_ord += 26
                key += chr(new_ord)
            res[key].append(string)
        return res.values()