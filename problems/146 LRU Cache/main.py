class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.len = 0
        self.directory = dict()

    def get(self, key: int) -> int:
        node = self.directory.get(key, None)
        if not node:
            return -1
        if node != self.head:
            # remove node from list
            if node == self.tail:
                node.prev.next = None
                self.tail = node.prev
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            # attach node as new head
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        return self.head.val

    def put(self, key: int, value: int) -> None:
        if key not in self.directory:
            node = Node(key, value, None, self.head)
            self.directory[key] = node
            if self.head:
                self.head.prev = node
            self.head = node
            if not self.tail:
                self.tail = node
            if self.len == self.capacity:
                del self.directory[self.tail.key]
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.len += 1
        else:
            self.directory[key].val = value
            self.get(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)