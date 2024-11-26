class Solution:

    def lower(self, c):
        isNum = ord('0') <= ord(c) <= ord('9') 
        isLow = ord('a') <= ord(c) <= ord('z')
        isUp = ord('A') <= ord(c) <= ord('Z')
        if isNum or isLow:
            return c
        if isUp:
            return chr(ord(c) - ord('A') + ord('a'))
        else:
            return None

    def isPalindrome(self, s: str) -> bool:
        sl = list(s)
        i, j = 0, 0
        for j in range(len(sl)):
            if lower(sl[j]):
                sl[i] = lower(sl[j])
                i += 1
        i, j = 0, i - 1
        while i < j:
            if sl[i] != sl[j]:
                return False
            i, j = i+1, j-1
        return True