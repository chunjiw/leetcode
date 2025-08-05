from heapq import heappush, heappop

class HitCounter:

    def __init__(self):
        self.pq = []

    def hit(self, timestamp: int) -> None:
        heappush(self.pq, timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.pq and self.pq[0] + 300 <= timestamp:
            heappop(self.pq)
        return len(self.pq)
    
hc = HitCounter()
hc.hit(1)
hc.hit(2)
hc.hit(3)
print(hc.getHits(4))
hc.hit(300)
print(hc.getHits(300))
print(hc.getHits(301))
        