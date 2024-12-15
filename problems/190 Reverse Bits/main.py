class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result |= ((n & 1) << (31 - i))
            n >>= 1
        return result

    def reverseBits2(self, n: int) -> int:
        for i in range(16):
            left = (n >> (31 - i)) & 1
            right = (n >> i) & 1
            if left == right:
                continue
            n ^= ((1 << i) | (1 << (31 - i)))
        return n