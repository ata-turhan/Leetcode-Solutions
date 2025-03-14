class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can_distribute(candy_count, candies, k):
            children_with_candies = 0

            for candy in candies:
                children_with_candies += candy // candy_count 
                if children_with_candies >= k:
                    return True

            return False

        left, right = 1, max(candies)
        max_candy = 0
        while left <= right:
            mid = left + (right - left) // 2
            if can_distribute(mid, candies, k):
                max_candy = mid 
                left = mid + 1
            else:
                right = mid - 1

        return max_candy
        