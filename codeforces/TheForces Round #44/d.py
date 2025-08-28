for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    steps = input()
    # replace all ? to L
    l, r = 0, 0
    p = 0
    for s in steps:
        if s == 'R':
            p += 1
            r = max(r, p)
        else:
            p -= 1
            l = min(l, p)
    if r - l + 1 > n:
        print('YES')
        print(steps.replace('?', 'L'))
        continue
    # replace all ? to R
    l, r = 0, 0
    p = 0
    for s in steps:
        if s == 'L':
            p -= 1
            l = min(l, p)
        else:
            p += 1
            r = max(r, p)
    if r - l + 1 > n:
        print('YES')
        print(steps.replace('?', 'R'))
        continue
    print('NO')
    