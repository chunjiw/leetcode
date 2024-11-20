# 67. Add Binary
# DescriptionHintsSubmissionsDiscussSolution
# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a
        
        res = []
        
        i, j = len(a) - 1, len(b) - 1
        extra = 0
        
        while i >= 0 or j >= 0:
            curr = extra
            if i >= 0:
                curr += int(a[i])
            if j >= 0:
                curr += int(b[j])
            if curr <= 1:
                res.append(str(curr))
                extra = 0
            else:
                res.append(str(curr % 2))
                extra = 1
            i -= 1
            j -= 1
        if extra:
            res.append('1')
        res.reverse()
        
        return ''.join(res)
        
