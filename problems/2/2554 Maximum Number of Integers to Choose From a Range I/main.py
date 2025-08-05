class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bag = set()
        for i in banned:
            bag.add(i)
        result = 0
        s = 0
        for i in range(1, n+1):
            if i in bag:
                continue
            if s + i > maxSum:
                return result
            else:
                s += i
                result += 1
        return result