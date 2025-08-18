from math import isqrt
from collections import Counter

class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        self.arr = arr
        n = len(arr)
        m = isqrt(n)                             # number of elements in each bucket
        nb = n // m + int(n % m > 0)    # number of bucket
        self.n, self.m, self.nb = n, m, nb
        self.freq = [Counter() for _ in range(nb)]
        for i in range(n):
            self.freq[i // m][arr[i]] += 1
                
    def query(self, left: int, right: int, value: int) -> int:
        n, m, nb = self.n, self.m, self.nb
        lb, rb = left // m, right // m
        if lb == rb:
            return Counter(self.arr[left:right+1])[value]
        cnt = 0
        for b in range(lb, rb+1):
            if b == lb:
                for i in range(left, (b+1)*m):
                    cnt += int(self.arr[i] == value)
            elif b == rb:
                for i in range(b*m, right+1):
                    cnt += int(self.arr[i] == value)
            else:
                cnt += self.freq[b][value]
            
        return cnt

fq = RangeFreqQuery([1,1,1,0,1,1,1,1,1,1,1,1])
print(fq.query(2, 5, 1))
print(fq.query(2, 5, 0))

fq = RangeFreqQuery([12,33,4,56,22,2,34,33,22,12,34,56])
print(fq.query(1,2,4))
print(fq.query(0,11,33))
