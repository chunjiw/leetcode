from sortedcontainers import SortedList

class Node:

    rank = 0

    def __init__(self, value):
        self.rank = Node.rank
        self.value = value
        Node.rank += 1

class MaxStack:

    def __init__(self):
        self.valueList = SortedList(key=lambda x: x.value)
        self.rankList = SortedList(key=lambda x: x.rank)

    def push(self, x: int) -> None:
        node = Node(x)
        self.valueList.add(node)
        self.rankList.add(node)

    def pop(self) -> int:
        node = self.rankList.pop()
        self.valueList.remove(node)
        return node.value
    
    def top(self) -> int:
        return self.rankList[-1].value

    def peekMax(self) -> int:
        return self.valueList[-1].value
    
    def popMax(self) -> int:
        node = self.valueList.pop()
        self.rankList.remove(node)
        return node.value
