class Solution:

    def pay(self, days, costs, k):
        if k in self.mem:
            return self.mem[k]
        if k == len(days):
            return 0
        cost0 = costs[0] + self.pay(days, costs, k + 1)
        g = k
        while g < len(days) and days[g] - days[k] < 7:
            g += 1
        cost1 = costs[1] + self.pay(days, costs, g)
        while g < len(days) and days[g] - days[k] < 30:
            g += 1
        cost2 = costs[2] + self.pay(days, costs, g)
        self.mem[k] = min((cost0, cost1, cost2))
        return self.mem[k]
        
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.mem = dict()
        return self.pay(days, costs, 0)