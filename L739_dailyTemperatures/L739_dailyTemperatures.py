# 739. Daily Temperatures
# DescriptionHintsSubmissionsDiscussSolution
# Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].


class Solution(object):
  def dailyTemperatures(self, temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    result = [0 for t in temperatures]
    stack = []
    for i, t in enumerate(temperatures):
      while stack and stack[-1][1] < t:
        ri, rt = stack.pop()
        result[ri] = i - ri
      stack.append((i, t))
    return result  
