class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        if not nums:
            return False
        if nums[0] == target or nums[-1] == target:
            return True
        
        i, j = 0, len(nums) - 1
        while j >= 0 and nums[i] == nums[j]:
            j -= 1
        if j < 0:
            return False
        
        while i < j:
            m = (i+j) // 2
            if nums[m] == target:
                return True
            if nums[i] <= target < nums[m] or target < nums[m] <= nums[j] or (nums[i] <= target and nums[m] <= nums[j]):
                j = m - 1
            else:
                i = m + 1
        
        return False
    
sol = Solution()
print(sol.search([2,5,6,0,0,1,2], 0))
print(sol.search([2,5,6,0,0,1,2], 3))
        
