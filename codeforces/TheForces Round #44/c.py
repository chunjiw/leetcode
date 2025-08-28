import math

def firstFactor(n, l, r):
    # factor n
    can = []
    for i in range(1, math.isqrt(n)+1):
        if n % i == 0:
            if l <= i <= r:
                return i
            elif i > r:
                return -1
            if i * i != n:
                can.append(n // i)
    while can:
        if l <= can[-1] <= r:
            return can[-1]
        can.pop()
    return -1

t = int(input())
for _ in range(t):
    n, l, r = [int(i) for i in input().split()]
    print(firstFactor(n, l, r))
