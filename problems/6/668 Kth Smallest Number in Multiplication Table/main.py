class Solution:

    def notbiggerthan(self, m, n, p):
        """Number of products that is not bigger than p; O(n)"""
        result = 0
        for i in range(1, n + 1):
            result += min(m, p // i)
        return result

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if n > m:
            m, n = n, m
        i, j = 1, m * n
        while i < j:
            p = i + (j - i) // 2
            if self.notbiggerthan(m, n, p) < k:
                i = p + 1
            else:
                j = p
        # here, i is the first number that self.notbiggerthan(i) >= k,
        # so self.notbiggerthan(i) == k, and i is the desired number.
        return i