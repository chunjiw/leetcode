# 208. Implement Trie (Prefix Tree)
# DescriptionHintsSubmissionsDiscussSolution
# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.




class Node(object):
    
    def __init__(self, char):
        self.val = char
        self.end = False
        self.next = []



class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            found = False
            for child in node.next:
                if char == child.val:
                    node = child
                    found = True
                    break
            if not found:
                node.next.append(Node(char))
                node = node.next[-1]
        node.end = True    
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            found = False
            for child in node.next:
                if char == child.val:
                    node = child
                    found = True
                    break
            if not found:
                return False
        return node.end
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            found = False
            for child in node.next:
                if char == child.val:
                    node = child
                    found = True
                    break
            if not found:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
