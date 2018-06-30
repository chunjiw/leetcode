# 190. Reverse Bits
# DescriptionHintsSubmissionsDiscussSolution
# Reverse bits of a given 32 bits unsigned integer.

# Example:

# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
#              return 964176192 represented in binary as 00111001011110000010100101000000.
# Follow up:
# If this function is called many times, how would you optimize it?


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if not n:
            return n
        for i in range(16):
            n = self.reversePair(n, i)
        return n
    
    def reversePair(self, n, i):
        right = (n >> i) & 1
        left = (n >> (31 - i)) & 1
        if left == right:
            return n
        else:
            return n ^ ((1 << i) + (1 << (31 - i)))
        
