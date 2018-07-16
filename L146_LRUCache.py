# 146. LRU Cache
# DescriptionHintsSubmissionsDiscussSolution
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


class Node(object):
    
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.key2node = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1
        node = self.key2node[key]
        self.changeHead(node)    
        return node.val
           
    def changeHead(self, node):
        if node is not self.head:
            if node is self.tail:
                # update tail
                node.prev.next = None
                self.tail = node.prev
            else:
                # update left and right
                node.prev.next = node.next
                node.next.prev = node.prev
            # update head
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node
            

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.key2node:
            node = self.key2node[key]
            node.val = value
            self.changeHead(node)
        else:        
            if self.size == self.capacity:
                # remove tail
                del self.key2node[self.tail.key]
                if self.size == 1:
                    self.head, self.tail = None, None
                else:
                    self.tail.prev.next = None
                    self.tail = self.tail.prev
                self.size -= 1
            # add new head
            node = Node(key, value)
            if self.size == 0:
                self.head, self.tail = node, node
            else:
                self.head.prev = node
                node.next = self.head
                node.prev = None
                self.head = node
            # update size
            self.size += 1
            # update map
            self.key2node[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
