class Solution:
    
    def build(self, arr, n, k):
        if len(arr) == n:
            self.count += 1
            if self.count == k:
                self.result = ''.join(arr)
            return
        for char in ('a', 'b', 'c'):
            if not arr or arr[-1] != char:
                arr.append(char)
                self.build(arr, n, k)
                arr.pop()

    def getHappyString(self, n: int, k: int) -> str:
        self.count = 0
        self.build([], n, k)
        if self.count < k:
            return ''
        return self.result

sol = Solution()
print(sol.getHappyString(1, 3))
print(sol.getHappyString(1, 4))
print(sol.getHappyString(3, 9))
print(sol.getHappyString(3, 13))