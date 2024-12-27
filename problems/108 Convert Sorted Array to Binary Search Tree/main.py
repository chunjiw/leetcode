# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def tree(self, nums, i, j):
        if i >= j:
            return
        if i + 1 == j:
            node = TreeNode(nums[i])
            return node
        m = i + (j - i) // 2
        node = TreeNode(nums[m])
        node.left = self.tree(nums, i, m)
        node.right = self.tree(nums, m + 1, j)
        return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.tree(nums, 0, len(nums))