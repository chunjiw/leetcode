#    a   b   c   d
#    1   a  ab  abc 
#   bcd  cd  d   1

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    incum = [1] * n
    for i in range(1, n):
      incum[i] = incum[i-1] * nums[i-1]
    decum = 1
    for i in range(n-2, -1, -1):
      decum *= nums[i+1]
      incum[i] *= decum
    return incum
