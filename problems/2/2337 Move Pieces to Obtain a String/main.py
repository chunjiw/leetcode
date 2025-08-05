class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i, j = 0, 0
        n = len(target)
        while i < n or j < n:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            if i < n and j < n:
                if start[i] != target[j]:
                    return False
                if start[i] == 'R' and i > j:
                    return False
                if start[i] == 'L' and i < j:
                    return False
            elif i < n or j < n:
                return False
            i, j = i+1, j+1
        return True

sol = Solution()
print(sol.canChange("_L__R__R_", "L______RR"))
print(sol.canChange("R_L_", "__LR"))
print(sol.canChange("_R", "R_"))