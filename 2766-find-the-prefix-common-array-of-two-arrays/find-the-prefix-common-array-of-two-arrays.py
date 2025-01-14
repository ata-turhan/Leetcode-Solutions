class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        Finds the prefix common array of two lists A and B.
        
        :param A: List[int] - First input list.
        :param B: List[int] - Second input list.
        :return: List[int] - Prefix common array where each index represents the number of common elements up to that point.
        """
        # List to store the result for the prefix common counts
        prefix_common_counts = []
        # Counter to keep track of elements encountered
        element_counts = defaultdict(int)
        # Tracks the total count of common elements found
        total_common_elements = 0

        # Iterate through elements of both lists simultaneously
        for element_a, element_b in zip(A, B):
            # Increment count for element from list A
            element_counts[element_a] += 1
            # If the element appears twice (once in A and once in B), it's common
            if element_counts[element_a] == 2:
                total_common_elements += 1

            # Increment count for element from list B
            element_counts[element_b] += 1
            # If the element appears twice (once in A and once in B), it's common
            if element_counts[element_b] == 2:
                total_common_elements += 1

            # Append the current count of common elements to the result
            prefix_common_counts.append(total_common_elements)

        return prefix_common_counts
