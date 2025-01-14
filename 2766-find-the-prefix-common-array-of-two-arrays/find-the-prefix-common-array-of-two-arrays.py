class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common_array = []
        prefix_count = 0
        num_counts = defaultdict(int)

        for a, b in zip(A, B):
            num_counts[a] += 1
            if num_counts[a] == 2:
                prefix_count += 1

            num_counts[b] += 1
            if num_counts[b] == 2:
                prefix_count += 1

            common_array.append(prefix_count)

        return common_array

            

        