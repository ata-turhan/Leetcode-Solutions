from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findPath(self, root: Optional[TreeNode], target: int, path: List[str]) -> bool:
        """
        Helper function to find the path to a target value in the binary tree.
        The path is recorded as a list of 'L' and 'R' directions.
        """
        if not root:
            return False
        if root.val == target:
            return True
        path.append('L')
        if self.findPath(root.left, target, path):
            return True
        path.pop()
        path.append('R')
        if self.findPath(root.right, target, path):
            return True
        path.pop()
        return False

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
        Function to find directions from the node with startValue to the node with destValue.
        """
        startPath, destPath = [], []
        
        # Find paths from the root to the startValue and destValue
        self.findPath(root, startValue, startPath)
        self.findPath(root, destValue, destPath)
        
        # Find the divergence point in the paths
        common_length = 0
        while common_length < len(startPath) and common_length < len(destPath) and startPath[common_length] == destPath[common_length]:
            common_length += 1
        
        # Steps to move up to the common ancestor
        stepsUp = 'U' * (len(startPath) - common_length)
        # Steps to move down to the destination
        stepsDown = ''.join(destPath[common_length:])
        
        return stepsUp + stepsDown
