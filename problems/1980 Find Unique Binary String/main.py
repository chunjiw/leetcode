class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = ['1' if nums[i][i] == '0' else '0' for i in range(len(nums))]
        return ''.join(result)