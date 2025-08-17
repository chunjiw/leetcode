class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        costUntil = [0] * (366+30)
        i = 0
        for day in range(1, 366):
            if day < days[i]:
                costUntil[day] = costUntil[day-1]
            elif day == days[i]:
                costUntil[day] = min((
                    costUntil[day-1] + costs[0],
                    costUntil[day-7] + costs[1],
                    costUntil[day-30] + costs[2]
                ))
                i += 1
                if i == len(days):
                    break
            else:
                error("should not reach here")
        return costUntil[days[-1]]