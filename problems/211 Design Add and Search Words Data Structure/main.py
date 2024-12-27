class Node:
    def __init__(self, val):
        self.val = val
        self.end = False
        self.next = dict()

class WordDictionary:

    def __init__(self):
        self.root = Node('')

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.next:
                node.next[char] = Node(char)
            node = node.next[char]
        node.end = True

    def search(self, word: str) -> bool:
        return self.searchfrom(self.root, word)

    def searchfrom(self, node, word) -> bool:
        for i, char in enumerate(word):
            if char == '.':
                return any([self.searchfrom(nextnode, word[i+1:]) for nextnode in node.next.values()])
            if char not in node.next:
                return False
            node = node.next[char]
        return node.end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)