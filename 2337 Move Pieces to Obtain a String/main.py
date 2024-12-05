class Solution:

    def segment(self, start, target) -> bool:
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

    def canChange(self, start: str, target: str) -> bool:
        if start == target:
            return True
        start = list(start)
        target = list(target)
        n = len(start)
        # look for transitions from R to L in target
        prev = None
        left = 0
        for i in range(n):
            if prev == 'R' and target[i] == 'L':
                # check segment (left, i - 1)
                if not self.segment(start[left : i], target[left : i]):
                    return False
                left = i
            if target[i] != '_':
                prev = target[i]
        return self.segment(start[left:], target[left:])

sol = Solution()
print(sol.canChange("_L__R__R_", "L______RR"))
print(sol.canChange("R_L_", "__LR"))
print(sol.canChange("_R", "R_"))