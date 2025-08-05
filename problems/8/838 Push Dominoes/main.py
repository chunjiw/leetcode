class Solution:
    def pushDominoes(self, dominoes):
        result = list(dominoes)
        start = 0
        right = False
        for (i, d) in enumerate(dominoes):
            if d == 'L':
                if not right:
                    for j in range(start, i):
                        result[j] = 'L'
                else:
                    a, b = start, i
                    while a < b:
                        result[a] = 'R'
                        result[b] = 'L'
                        a += 1
                        b -= 1
                right = False
                start = i
            elif d == 'R':
                if right:
                    for j in range(start, i):
                        result[j] = 'R'                                                                                                                                                      
                start = i
                right = True
        if right:
            for j in range(start, len(dominoes)):
                result[j] = 'R'
        return ''.join(result)

sol = Solution()
print(sol.pushDominoes('RR.L'))
print(sol.pushDominoes('RR..L'))
print(sol.pushDominoes('.L.R...LR..L..'))
print(sol.pushDominoes(".L.R."))
print(sol.pushDominoes("R.R.L"))
