class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        ugly_nums = set()
        for _ in range(n):
            ugly_num = heapq.heappop(heap)
            if ugly_num * 2 not in ugly_nums:
                heapq.heappush(heap, ugly_num * 2)
                ugly_nums.add(ugly_num * 2)
            if ugly_num * 3 not in ugly_nums:
                heapq.heappush(heap, ugly_num * 3)
                ugly_nums.add(ugly_num * 3)
            if ugly_num * 5 not in ugly_nums:
                heapq.heappush(heap, ugly_num * 5)
                ugly_nums.add(ugly_num * 5)

            print(ugly_num)
            
        return ugly_num
        