from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

class Solution:

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generate(1, n)

    def generate(self, m: int, n: int):
        """Returns all BSTs that has nodes from m to n, inclusive
        """
        result = []
        if m == n:
            result.append(TreeNode(m))
        for root in range(m, n+1):
            # print(m, n, root)
            left_list = self.generate(m, root - 1)
            right_list = self.generate(root + 1, n)
            if not left_list and not right_list:
                continue
            if not left_list:
                left_list.append(None)
            if not right_list:
                right_list.append(None)
            for left in left_list:
                for right in right_list:
                    result.append(TreeNode(root, left, right))
        return result

sol = Solution()
print(sol.generateTrees(3))