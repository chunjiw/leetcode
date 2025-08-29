class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Alice wins with odd number of flowers
        
        n0 = n // 2
        n1 = n // 2 + n % 2
        m0 = m // 2
        m1 = m // 2 + m % 2

        return n0*m1 + n1*m0

sol = Solution()
print(sol.flowerGame(3,2))
print(sol.flowerGame(1,1))