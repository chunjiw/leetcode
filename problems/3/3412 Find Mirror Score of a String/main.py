class Solution:

    def mirror(self, ch):
        return chr(25 - (ord(ch) - ord('a')) + ord('a'))
    
    def calculateScore(self, s: str) -> int:
        map = dict()
        score = 0
        for (i, char) in enumerate(s):
            indices = map.get(char, [])
            if indices:
                j = indices.pop()
                score += i - j
            else:
                indices = map.get(self.mirror(char), [])
                indices.append(i)
                map[self.mirror(char)] = indices
        return score
