# 356. Line Reflection
# DescriptionHintsSubmissionsDiscussSolution
# Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

# Example 1:
# Given points = [[1,1],[-1,1]], return true.

# Example 2:
# Given points = [[1,1],[-1,-1]], return false.

# Follow up:
# Could you do better than O(n2)?

# Credits:
# Special thanks to @memoryless for adding this problem and creating all test cases.




class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        midx = (min([x for x, y in points]) + max([x for x, y in points])) / 2.0
        s = set()
        for x, y in points:
            s.add((x,y))
        print s
        for x, y in points:
            if (2 * midx - x, y) not in s:
                return False
        return True            
