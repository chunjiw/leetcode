def canPass(segments: list[list[int]], k):
    a, b = 0, 0
    for l, r in segments:
        if b+k < l or a-k > r:
            return False
        else:
            # intersection of [a-k, b+k] and [l, r]
            a, b = max(a-k, l), min(b+k, r)
    return True

def minK(segments: list[list[int]]) -> int:
    # binary search on k
    i, j = 0, 10**9
    while i < j:
        m = (i+j) // 2
        if canPass(segments, m):
            j = m
        else:
            i = m + 1
    return i

ntests = int(input())
for _ in range(ntests):
    n = int(input())
    segments = []
    for _ in range(n):
        segments.append([int(i) for i in input().split()])
    print(minK(segments))