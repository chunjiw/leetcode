class Solution:
  def hIndex(self, citations: List[int]) -> int:
    citations.sort(reverse=True)
    m = 0
    for i in range(len(citations)):
      if citations[i] > i:
        m += 1
    return m
