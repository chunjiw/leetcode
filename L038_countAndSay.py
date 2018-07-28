# 38. Count and Say
# DescriptionHintsSubmissionsDiscussSolution
# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.

# Example 1:

# Input: 1
# Output: "1"
# Example 2:

# Input: 4
# Output: "1211"

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        seq = [1]
        for _ in range(n - 1):
            seq = self.next(seq)
        seq = [str(c) for c in seq]
        return ''.join(seq)
    
    def next(self, seq):
        result = []
        count = 0
        curr = seq[0]
        for item in seq:
            if curr == item:
                count += 1
            else:
                result.append(count)
                result.append(curr)
                curr = item
                count = 1
        if count:
            result.append(count)
            result.append(curr)
        return result        
