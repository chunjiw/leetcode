from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.basic = [set() for _ in range(numCourses)]
        self.advance = [set() for _ in range(numCourses + 1)]
        for a, b in prerequisites:
            self.basic[a].add(b)
            self.advance[b].add(a)
        # Create fake most basic course as course `numCourses`
        for a in range(numCourses):
            if not self.basic[a]:
                self.basic[a].add(numCourses)
                self.advance[numCourses].add(a)
        # Go from most basic course `numCourses` and BFS
        order = [-2] * (numCourses + 1)    # -2 means not learned yet
        order[numCourses] = -1
        queue = deque([numCourses])
        day = -1
        while queue:
            for _ in range(len(queue)):
                a = queue.popleft()
                for b in self.advance[a]:
                    if order[b] == -2 and all([order[c] > -2 for c in self.basic[b]]):
                        day += 1
                        order[b] = day
                        queue.append(b)
        if day != numCourses - 1:
            return []
        result = [0] * numCourses
        for course, day in enumerate(order):
            if day >= 0:
                result[day] = course
        return result
            
