class Solution:

    def __init__(self):
        self.result = dict()

    def numTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n < 2:
            return 1
        if n in self.result:
            return self.result[n]
        result = 0
        for root in range(1, n+1):
            left = self.numTrees(root - 1)
            right = self.numTrees(n - root)
            result += left * right
        self.result[n] = result
        return result