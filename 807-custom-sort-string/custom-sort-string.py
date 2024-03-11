class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sort_order = defaultdict(int)
        for i, char in enumerate(order):
            sort_order[char] = i
        return "".join(sorted(list(s), key=lambda char:sort_order[char]))

        