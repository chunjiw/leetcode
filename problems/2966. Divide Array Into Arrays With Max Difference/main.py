class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        while nums:
            sub = []
            sub.append(nums.pop())
            sub.append(nums.pop())
            sub.append(nums.pop())
            if sub[0] - sub[-1] > k:
                return []
            res.append(sub)
        return res