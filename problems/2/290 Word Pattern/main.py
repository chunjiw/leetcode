class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1 = dict()
        d2 = dict()
        k = 0
        i, j = 0, 0
        while k < len(pattern) and i < len(s):
            # get word in s
            while j < len(s) and s[j] != ' ':
                j += 1
            word = s[i:j]
            p = pattern[k]
            if p not in d1:
                d1[p] = word
            elif d1[p] != word:
                return False
            if word not in d2:
                d2[word] = p
            elif d2[word] != p:
                return False
            k += 1
            i = j + 1
            j += 1
        if k != len(pattern) or i != len(s) + 1:
            return False
        return True