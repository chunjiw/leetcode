class Solution(object):
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        n = len(nums)
        nums.sort()
        result = {}

        def kSum(k, start, target, candidate):
            """
            look for k-sum in nums[start:]
            """

            if k == 2:
                bag = set()
                for i in range(start, n):
                    if target - nums[i] in bag:
                        can = list(sorted(candidate + [nums[i], target - nums[i]]))
                        result[str(can)] = can
                    bag.add(nums[i])
                return
            for i in range(start, n):
                kSum(k-1, i+1, target - nums[i], candidate + [nums[i]])
            
        kSum(4, 0, target, [])
        return list(result.values())
    
sol = Solution()
print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))

# -2 -1 0 0 1 2
# i                    k = 4   
#    i                 k = 3
#       i              k = 2   target = 3