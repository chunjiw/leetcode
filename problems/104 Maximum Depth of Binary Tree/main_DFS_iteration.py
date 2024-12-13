class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 0
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            while node:
                if node.right:
                    stack.append((node.right, depth+1))
                node = node.left
                depth += 1
            result = max(result, depth)
        return result
