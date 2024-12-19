from typing import List

from collections import deque

class Solution:

    def getKey(self, word, i):
        keyList = list(word)
        keyList[i] = '_'
        return ''.join(keyList)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        book = dict()
        for word in wordList:
            for i in range(len(word)):
                key = self.getKey(word, i)
                value = book.get(key, set())
                value.add(word)
                book[key] = value
        queue = deque([beginWord])
        seen = set(queue)
        steps = 1
        while queue:
            steps += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    key = self.getKey(word, i)
                    for nextword in book.get(key, []):
                        if nextword == endWord:
                            return steps
                        if nextword not in seen:
                            queue.append(nextword)
                            seen.add(nextword)
        return 0

sol = Solution()
result = sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
result = sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])
print(result)