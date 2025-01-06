class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        result = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                a = nums[i] + nums[j]
                if a + nums[j+1] >= target:
                    break
                # search for last k such that a + nums[k] < target
                if a + nums[n-1] < target:
                    result += n - 1 - j
                    continue
                # here, guarantee there exists p such that a + nums[p] >= target
                l, r = j + 1, n - 1
                while l < r:
                    m = l + (r - l) // 2
                    if a + nums[m] < target:
                        l = m + 1
                    else:
                        r = m
                # here, l is the first such that a + nums[l] >= target
                result += l - 1 - j
        return result