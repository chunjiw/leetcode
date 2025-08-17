class Solution:

    def isAlphanumeric(self, c):
        isNum = ord('0') <= ord(c) <= ord('9') 
        isLow = ord('a') <= ord(c) <= ord('z')
        isUp = ord('A') <= ord(c) <= ord('Z')
        return isNum or isLow or isUp
    
    def similar(self, c1, c2):
        return c1.lower() == c2.lower()

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not self.isAlphanumeric(s[i]):
                i += 1
                continue
            if not self.isAlphanumeric(s[j]):
                j -= 1
                continue
            if not self.similar(s[i], s[j]):
                return False
            i, j = i+1, j-1
        return True