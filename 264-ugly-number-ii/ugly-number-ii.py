import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]  # Min-heap to store the next potential ugly numbers
        seen = {1}  # Set to keep track of numbers that have been added to the heap

        for _ in range(n):
            # Extract the smallest ugly number from the heap
            ugly_num = heapq.heappop(heap)

            # Generate the next potential ugly numbers by multiplying with 2, 3, and 5
            for factor in [2, 3, 5]:
                new_ugly = ugly_num * factor
                if new_ugly not in seen:
                    heapq.heappush(heap, new_ugly)
                    seen.add(new_ugly)

        return ugly_num  # The nth ugly number
