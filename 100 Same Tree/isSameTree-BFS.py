# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pline = [p]
        qline = [q]
        while pline:
            p = pline.pop(0)
            q = qline.pop(0)
            if p is None and q is None:
                continue
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            pline.append(p.left)
            pline.append(p.right)
            qline.append(q.left)
            qline.append(q.right)
        return True
