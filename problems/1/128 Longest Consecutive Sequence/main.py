from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start, end = dict(), dict()
        seen = set()
        result = 0
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            if num + 1 in start and num - 1 in end:
                l = start.pop(num + 1)
                l0 = end.pop(num - 1)
                l[0] = l0[0]
                start[l[0]] = l
            elif num + 1 in start:
                l = start.pop(num + 1)
                l[0] = num
                start[num] = l
            elif num - 1 in end:
                l = end.pop(num - 1)
                l[-1] = num
                end[num] = l
            else:
                l = [num, num]
                start[num] = l
                end[num] = l
            # print(num, l, start, end)
            result = max(result, l[-1] - l[0] + 1)
        return result
            
sol = Solution()
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(sol.longestConsecutive([-7,-1,3,-9,-4,7,-3,2,4,9,4,-9,8,-7,5,-1,-7]))
print(sol.longestConsecutive([3,2,4,4,5]))


