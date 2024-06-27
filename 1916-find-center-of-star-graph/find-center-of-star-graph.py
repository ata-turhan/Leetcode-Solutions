class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Find the common node between the first two edges
        return (set(edges[0]) & set(edges[1])).pop()
