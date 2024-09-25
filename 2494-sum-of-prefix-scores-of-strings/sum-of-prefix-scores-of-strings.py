class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefixes = defaultdict(int)
        for word in words:
            prefix = ""
            for char in word:
                prefix += char
                prefixes[prefix] += 1
        counts = []
        for word in words:
            prefix = ""
            count = 0
            for char in word:
                prefix += char
                count += prefixes[prefix]
            counts.append(count)
        return counts
                
        