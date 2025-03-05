class Solution:
    def coloredCells(self, layers: int) -> int:
        """Computes the total number of colored cells in an expanding pattern."""
        return layers**2 + (layers - 1)**2
