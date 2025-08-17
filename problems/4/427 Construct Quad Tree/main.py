"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:

    def build(self, grid, i, j, s):
        if s == 1:
            return Node(grid[i][j], True, None, None, None, None)
        ss = s // 2
        topLeft = self.build(grid, i, j, ss)
        topRight = self.build(grid, i, j+ss, ss)
        botLeft = self.build(grid, i+ss, j, ss)
        botRight = self.build(grid, i+ss, j+ss, ss)
        if topLeft.val == topRight.val == botLeft.val == botRight.val == 1:
            return Node(1, True, None, None, None, None)
        elif topLeft.val == topRight.val == botLeft.val == botRight.val == 0:
            return Node(0, True, None, None, None, None)
        else:
            return Node(-1, False, topLeft, topRight, botLeft, botRight)
    
    def revalue(self, node):
        if node.isLeaf:
            return
        if node.val == -1:
            node.val = 0
            self.revalue(node.topLeft)
            self.revalue(node.topRight)
            self.revalue(node.bottomLeft)
            self.revalue(node.bottomRight)

    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        root = self.build(grid, 0, 0, n)
        self.revalue(root)
        return root
