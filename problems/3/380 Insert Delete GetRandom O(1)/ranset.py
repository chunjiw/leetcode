import random

class RandomizedSet:

    def __init__(self):
        self.index = dict()
        self.vals = list()        

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.index[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        idx = self.index.pop(val)
        if idx == len(self.vals) - 1:
            self.vals.pop()
        else:
            self.vals[idx] = self.vals.pop()
            self.index[self.vals[idx]] = idx
        return True

    def getRandom(self) -> int:
        i = random.randint(0, len(self.vals) - 1)
        return self.vals[i]
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print()

print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print()

print(obj.remove(1))
print(obj.insert(2))
print()

print(obj.getRandom())
print(obj.getRandom())
