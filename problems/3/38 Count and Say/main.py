class Solution:
    def countAndSay(self, n: int) -> str:

        arr = [1]

        for _ in range(n-1):
            stack = []
            count = []
            for d in arr:
                if not stack or stack[-1] != d:
                    stack.append(d)
                    count.append(1)
                else:
                    count[-1] += 1
            arr = []
            for i in range(len(stack)):
                arr.append(count[i])
                arr.append(stack[i])
        return ''.join(str(d) for d in arr)
    
sol = Solution()
print(sol.countAndSay(1))
print(sol.countAndSay(2))
print(sol.countAndSay(3))
print(sol.countAndSay(4))
print(sol.countAndSay(5))
print(sol.countAndSay(6))
print(sol.countAndSay(7))
print(sol.countAndSay(8))