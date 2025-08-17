class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        a, b = zero, one
        modulo = 1000000007
        result = 0
        if a > b:
            a, b = b, a
        queue = deque([0] * b)
        queue[b-a] = 1
        end = a - 1
        while end < high:
            queue.append((queue[0] + queue[b-a]) % modulo)
            queue.popleft()
            end += 1
            if end >= low:
                result = (result + queue[-1]) % modulo
        return result
        