class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    incum = list(nums)    # increasing cum prod; incum[n-1] is not used
    decum = list(nums)    # decreasing cum prod; decum[0] is not used
    for i in range(1, n-1):
      incum[i] = incum[i-1] * nums[i]
      decum[-i-1] = decum[-i] * nums[-i-1]
    result = list(nums)
    result[0] = decum[1]
    result[-1] = incum[-2]
    for i in range(1, n-1):
      result[i] = incum[i-1] * decum[i+1]
    return result