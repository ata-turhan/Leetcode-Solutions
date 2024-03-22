class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(re.split(r"\s+", s.strip())))
        