# 247. Strobogrammatic Number II
# DescriptionHintsSubmissionsDiscussSolution
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Find all strobogrammatic numbers that are of length = n.

# Example:

# Input:  n = 2
# Output: ["11","69","88","96"]


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return []
        if n % 2:
            return self.wrap(["1", "0", "8"], n - 1)
        else:
            return self.wrap([""], n)
    
    def wrap(self, toWrap, n):
        if n == 0:
            return toWrap
        
        result = []
        if n == 2:
            for num in toWrap:
                result += ['1' + num + '1', '6' + num + '9', '8' + num + '8', '9' + num + '6']
            return result
        else:
            for num in toWrap:
                result += ['1' + num + '1', '6' + num + '9', '8' + num + '8', '9' + num + '6', '0' + num + '0']
            return self.wrap(result, n - 2)
            
