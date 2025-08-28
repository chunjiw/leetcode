ntests = int(input())
for _ in range(ntests):

    n, m = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]

    zeros = []
    digits = 0

    for num in nums:
        zeroCount = 0
        while num % 10 == 0:
            zeroCount += 1
            num //= 10
        while num:
            num //= 10
            digits += 1
        if zeroCount > 0:
            zeros.append(zeroCount)
    
    zeros.sort(reverse=True)
    digits += sum(zeros[1::2])

    if digits > m:
        print('Sasha')
    else:
        print('Anna')
        