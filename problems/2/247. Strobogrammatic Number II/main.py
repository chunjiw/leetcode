class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:
        res = []

        stack = [''] if n % 2 == 0 else ['0', '1', '8']
        if n == 1:
            return stack
        while stack:
            stem = stack.pop()
            if len(stem) == n and stem[0] != '0':
                res.append(stem)
            elif len(stem) < n:
                for a,b in ['69','96','00','11','88']:
                    stack.append(a + stem + b)

        return res        
    
sol = Solution()
print(sol.findStrobogrammatic(1))
print(sol.findStrobogrammatic(2))
print(sol.findStrobogrammatic(3))
print(sol.findStrobogrammatic(4))
print(sol.findStrobogrammatic(5))