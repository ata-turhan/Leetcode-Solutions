class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = defaultdict(lambda:-1)
        colors_count = defaultdict(int)
        res = []
        distinct_colors = 0

        for query in queries:
            ball_idx, color = query
            if balls[ball_idx] != -1:
                colors_count[balls[ball_idx]] -= 1
                if colors_count[balls[ball_idx]] == 0:
                    distinct_colors -= 1
            
            balls[ball_idx] = color
            colors_count[color] += 1

            if colors_count[color] == 1:
                distinct_colors += 1

            res.append(distinct_colors)

        return res


        