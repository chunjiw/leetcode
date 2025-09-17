from collections import defaultdict
from heapq import heapify, heappush, heappop

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.group: defaultdict[str, list[tuple[int, str]]] = defaultdict(list)
        self.rate = {}
        self.cuisine = {}
        n = len(foods)
        for i in range(n):
            food, cuis, rate = foods[i], cuisines[i], ratings[i]
            self.rate[food] = rate
            self.cuisine[food] = cuis
            self.group[cuis].append((-rate, food))
        for heap in self.group.values():
            heapify(heap)

    def changeRating(self, food: str, newRating: int) -> None:
        cuis = self.cuisine[food]
        heappush(self.group[cuis], (-newRating, food))
        self.rate[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        g = self.group[cuisine]
        while -g[0][0] != self.rate[g[0][1]]:
            heappop(g)
        return g[0][1]        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)