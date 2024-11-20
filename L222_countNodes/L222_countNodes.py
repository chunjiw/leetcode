# 222. Count Complete Tree Nodes
# DescriptionHintsSubmissionsDiscussSolution
# Given a complete binary tree, count the number of nodes.

# Note:

# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Example:

# Input: 
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6

# Output: 6



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # approach: binary search O(log(n)^2)
        if not root:
            return 0
        # get height
        h = 0
        left = root.left
        while left:
            left = left.left
            h += 1
        # corner cases
        if h == 0:
            return 1
        if h == 1:
            if root.right:
                return 3
            else:
                return 2
        # binary search
        left, right = 0, 2**h - 1
        if not self.isNull(right, root, h):
            return 2 ** (h + 1) - 1
        while left < right - 1:
            mid = (left + right) / 2
            print left, right, mid
            if self.isNull(mid, root, h):
                right = mid
            else:
                left = mid
        return 2**h - 1 + right
            
            
    def isNull(self, index, root, h):
        seq = []
        print index
        while index:
            seq.append(index % 2) 
            index /= 2
        while len(seq) != h:
            seq.append(0)
        seq.reverse()
        print index, "seq: ", seq
        for b in seq:
            if not root:
                print "error"
            if b:
                root = root.right
            else:
                root = root.left
        return root == None
