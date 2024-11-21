class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            gas[i] -= cost[i]
            if i > 0:
                gas[i] += gas[i-1]
        if gas[-1] < 0:
            return -1
        prev = 0
        mingas = 0
        index = 0
        for i in range(n):
            delta = gas[i] - prev
            if delta >= 0 and prev <= mingas:
                mingas = prev
                index = i
            prev = gas[i]
        return index