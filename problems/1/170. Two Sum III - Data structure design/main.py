class TwoSum:

    def __init__(self):
        self.bag = Counter()
        

    def add(self, number: int) -> None:
        self.bag[number] += 1

    def find(self, value: int) -> bool:
        for num, rep in self.bag.items():
            if value - num == num:
                if rep >= 2:
                    return True
            elif value - num in self.bag:
                return True
        return False
                


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)