class Node:

    def __init__(self, val):
        self.val = val
        self.isEnd = False
        self.next = dict()
    
class Trie:

    def __init__(self):
        self.root = Node('')
        
    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.next:
                node.next[letter] = Node(letter)
            node = node.next[letter]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.next:
                return False
            node = node.next[letter]
        return node.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.next:
                return False
            node = node.next[letter]
        return True
