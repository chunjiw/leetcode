class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        candidate = [True] * n
        for e in edges:
            candidate[e[1]] = False
        if sum(candidate) == 1:
            return candidate.index(True)
        else:
            return -1
