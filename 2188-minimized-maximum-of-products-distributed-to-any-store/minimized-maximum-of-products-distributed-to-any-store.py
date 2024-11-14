class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(size):
            store_counts = 0
            for quantity in quantities:
                store_counts += math.ceil(quantity / size)
            return store_counts <= n

        left, right = 1, max(quantities)
        min_max_count = right + 1
        while left <= right:
            mid = (left + right) // 2
            if can_distribute(mid):
                min_max_count = min(min_max_count, mid)
                right = mid - 1  
            else:
                left = mid + 1      

        return min_max_count