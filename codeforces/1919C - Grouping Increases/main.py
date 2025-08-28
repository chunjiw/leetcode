
def minPenalty(nums: list[int]) -> int:
    n = len(nums)
    if n < 3:
        return 0
    res = 0
    h1, h2 = nums[0], None
    for i in range(1, n):
        num = nums[i]
        if not h2:
            if num <= h1:
                h1 = num
            else:
                h1, h2 = num, h1
        else:
            if num <= h2:
                h2 = num
            elif num <= h1:
                h1 = num
            else:
                h1, h2 = num, h1
                res += 1
    return res

ntests = int(input())
for _ in range(ntests):
    n = int(input())
    nums = [int(i) for i in input().split()]
    print(minPenalty(nums))