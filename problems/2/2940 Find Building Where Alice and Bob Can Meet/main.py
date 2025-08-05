from typing import List

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        for query in queries:
            if query[0] > query[1]:
                query[0], query[1] = query[1], query[0]
        sortedqueries = [(i, q) for (i, q) in enumerate(queries)]
        sortedqueries.sort(key = lambda x: x[1][1])
        queries = sortedqueries
                
        ans = [0] * len(sortedqueries)

        n = len(heights)
        stack = []
        nexthigher = [0] * n
        for i in range(n-1, -1, -1):
            num = heights[i]
            while stack and num >= heights[stack[-1]]:
                stack.pop()
            nexthigher[i] = stack[-1] if stack else -1
            stack.append(i)
            # look for ans in stack
            while queries and queries[-1][1][1] == i:
                j, query = queries.pop()
                a, b = query
                if a == b or heights[a] < heights[b]:
                    ans[j] = b
                elif heights[a] == heights[b]:
                    ans[j] = nexthigher[b]
                else:
                    left = 0
                    right = len(stack) - 2
                    while left < right:
                        m = left + (right - left) // 2
                        if heights[stack[m]] > heights[a]:
                            left = m + 1
                        else:
                            right = m
                    # print("---", left, right, stack, stack[left], heights[stack[left]], heights[a], j)
                    if left > 0 and heights[stack[left]] <= heights[a]:
                        ans[j] = stack[left - 1]
                    elif heights[stack[left]] <= heights[a]:
                        ans[j] = -1
                    else:
                        ans[j] = stack[left]
        return ans
        
sol = Solution()
print(sol.leftmostBuildingQueries([6,4,8,5,2,7], [[0,1],[0,3],[2,4],[3,4],[2,2]]))
