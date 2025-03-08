class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolor = k

        white_count = blocks[:k].count("W")
        min_recolor = min(min_recolor, white_count)
        
        for i in range(k, len(blocks)):
            if blocks[i - k] == "W":
                white_count -= 1
            if blocks[i] == "W":
                white_count += 1

            min_recolor = min(min_recolor, white_count)

        return min_recolor        