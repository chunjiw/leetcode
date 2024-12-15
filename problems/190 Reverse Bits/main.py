class Solution:
    def reverseBits(self, n: int) -> int:
        for i in range(16):
            left = (n >> (31 - i)) & 1
            right = (n >> i) & 1
            if left == right:
                continue
            n ^= ((1 << i) | (1 << (31 - i)))
        return n
