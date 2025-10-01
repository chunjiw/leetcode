class Solution:
    def distinctPoints(self, s: str, k: int) -> int:

        def move(d, x, y, reverse=False):
            dx, dy = 0, 0
            if d == 'U':
                dy += 1
            elif d == 'D':
                dy -= 1
            elif d == 'L':
                dx -= 1
            else:
                dx += 1
            if reverse:
                dx, dy = -dx, -dy
            return (x+dx, y+dy)

        n = len(s)
        x, y = 0, 0
        for i in range(k, n):
            x, y = move(s[i], x, y)
        bag = { (x,y) }
        for i in range(n-k):
            x, y = move(s[i], x, y)
            x, y = move(s[i+k], x, y, True)
            bag.add((x,y))
        
        return len(bag)
    
sol = Solution()
print(sol.distinctPoints('UDLR', 4))
print(sol.distinctPoints('UU', 1))
print(sol.distinctPoints('ULU', 1))
