# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minmax(self, root, mindiff):
        mi, ma = root.val, root.val
        if root.left:
            mi, leftmax = self.minmax(root.left, mindiff)
            mindiff[0] = min(mindiff[0], root.val - leftmax)
        if root.right:
            rightmin, ma = self.minmax(root.right, mindiff)
            mindiff[0] = min(mindiff[0], rightmin - root.val)
        return mi, ma

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mindiff = [1000000]
        self.minmax(root, mindiff)
        return mindiff[0]
        