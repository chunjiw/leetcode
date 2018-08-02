# 316. Remove Duplicate Letters
# DescriptionHintsSubmissionsDiscussSolution
# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# Example 1:

# Input: "bcabc"
# Output: "abc"
# Example 2:

# Input: "cbacdcbc"
# Output: "acdb"


from collections import Counter

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        c = Counter(s)
        stack = []
        stackset = set()
        fixed = set()
        for l in s:
            # print l, stack, fixed, c
            if not c[l]:
                continue
            if l in stackset:
                c[l] -= 1
                if not c[l]:
                    fixed.add(l)
                continue    
            while stack and l < stack[-1] and stack[-1] not in fixed:
                stackset.remove(stack.pop())
            stack.append(l)
            stackset.add(l)
            c[l] -= 1
            if not c[l]:
                fixed.add(l)           
        return ''.join(stack)
                
            
