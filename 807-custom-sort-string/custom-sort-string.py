class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_index = defaultdict(int)

        # Create a dictionary to store the index of each character in the order string
        for i, char in enumerate(order):
            order_index[char] = i

        # Sort the characters in string s based on their indices in the order string
        sorted_s = sorted(s, key=lambda char: order_index[char])

        # Join the sorted characters to form the final string
        return "".join(sorted_s)
