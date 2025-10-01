class Solution:
    def maxAlternatingSum(self, nums: list[int], swaps: list[list[int]]) -> int:
        bag = set()
        for p, q in swaps:
            bag.add(p)
            bag.add(q)
        nc = sum(p%2 for p in bag)
        pc = len(bag) - nc

        snums = list(sorted(nums[p] for p in bag))
        res = sum(snums[-pc:]) - sum(snums[:-pc])

        for i in range(len(nums)):
            if i not in bag:
                res += nums[i] * (1-2*(i%2))
        
        return res
    
sol = Solution()
print(sol.maxAlternatingSum([1,2,3], [[0,2],[1,2]]))
print(sol.maxAlternatingSum([1,2,3], [[1,2]]))