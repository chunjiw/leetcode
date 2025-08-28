def aliceWin(n, x, y):
    if x > y:
        x, y = -x, -y
    while x+1 <= y:
        # Alice moves
        if x+1 == y:
            print('NO')
            return
        if y - x > 3:
            x += 3
        elif y - x > 1:
            x += 1
        # Bob moves
        if x+1 == y:
            print('YES')
            return
        if y - x > 3:
            y -= 3
        elif y - x > 1:
            y -= 1


ntests = int(input())
for _ in range(ntests):
    n, x, y = [int(i) for i in input().split()]
    aliceWin(n, x, y)