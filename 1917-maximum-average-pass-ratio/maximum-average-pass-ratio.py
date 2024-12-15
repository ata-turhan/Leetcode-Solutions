from heapq import heappush, heappop

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Function to calculate the improvement in pass ratio if one extra student is added
        def improvement(passed: int, total: int) -> float:
            return (passed + 1) / (total + 1) - passed / total

        # Max-heap to prioritize classes based on improvement
        max_heap = []
        
        # Initialize the heap with negative improvement to use Python's min-heap as max-heap
        for passed, total in classes:
            heappush(max_heap, (-improvement(passed, total), passed, total))
        
        # Assign all extra students
        for _ in range(extraStudents):
            # Pop the class with the maximum potential improvement
            neg_imp, passed, total = heappop(max_heap)
            # Add one student to the class
            passed += 1
            total += 1
            # Push the updated class back into the heap
            heappush(max_heap, (-improvement(passed, total), passed, total))
        
        # Calculate the final average pass ratio
        total_ratio = sum(passed / total for _, passed, total in max_heap)
        return total_ratio / len(classes)

        