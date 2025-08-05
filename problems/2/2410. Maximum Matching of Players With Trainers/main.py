from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res = 0
        while players and trainers:
            p = players.pop()
            if p <= trainers[-1]:
                trainers.pop()
                res += 1
        return res

sol = Solution()
print(sol.matchPlayersAndTrainers([4,7,9], [8,2,5,8]))