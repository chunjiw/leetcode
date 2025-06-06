class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for n in arr:
            if 2 * n in s or n / 2 in s:
                return True
            else:
                s.add(n)
        return False