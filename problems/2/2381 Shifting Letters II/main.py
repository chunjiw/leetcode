class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        delta = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            d = 1 if direction == 1 else -1
            delta[start] += d
            delta[end + 1] -= d
        for i in range(1, len(delta)):
            delta[i] += delta[i-1]
        ss = [chr((ord(s[i]) - ord('a') + delta[i]) % 26 + ord('a')) for i in range(len(s))]
        return ''.join(ss)