from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = dict()
        for a, b in prerequisites:
            a_set = graph.get(a, [])
            a_set.append(b)
            graph[a] = a_set
        if not graph:
            return True
        for start, _ in prerequisites:
            print(f"start from {start}")
            stack = [start]
            seen = set(stack)
            while stack:
                print(stack, seen)
                node = stack.pop()
                for nei in graph[node]:
                    if nei in graph:
                        if nei in seen:
                            return False
                        seen.add(nei)
                        stack.append(nei)
        return True
        
sol = Solution()
# print(sol.canFinish(2, [[1,0]]))
print(sol.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))