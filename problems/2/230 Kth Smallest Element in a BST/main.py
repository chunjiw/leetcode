# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder(self, root, count, k):
        if not root:
            return
        self.inorder(root.left, count, k)
        count[0] += 1
        if count[0] == k:
            count.append(root.val)
        self.inorder(root.right, count, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        self.inorder(root, count, k)
        return count[1]
