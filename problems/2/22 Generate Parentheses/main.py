from typing import List

class Solution:

    def build(self, left, right):
        if left == right == 0:
            self.results.append(''.join(self.result))
            return
        if left > 0:
            self.result.append('(')
            self.build(left - 1, right)
            self.result.pop()
        if left < right:
            self.result.append(')')
            self.build(left, right - 1)
            self.result.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.results = []
        self.result = []
        self.build(n, n)
        return self.results

sol = Solution()
print(sol.generateParenthesis(1))
print(sol.generateParenthesis(2))
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(4))
