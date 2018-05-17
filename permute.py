# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.pm(0, nums, result)
        return result

    def pm(self, index, solution, result):
        if index == len(solution):
            result.append(list(solution))
            return
        for i in range(index, len(solution)):
            solution[i], solution[index] = solution[index], solution[i]
            self.pm(index + 1, solution, result)
            solution[i], solution[index] = solution[index], solution[i]
