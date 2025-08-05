class Solution:

    def dfs(self, node, path):
        if node in path:
            return False
        if node in self.seen:
            return True
        path.add(node)
        self.seen.add(node)
        for child in self.graph[node]:
            if not self.dfs(child, path):
                return False
        path.remove(node)
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = [set() for _ in range(numCourses)]
        for a, b in prerequisites:
            self.graph[a].add(b)
        self.seen = set()
        for a in range(numCourses):
            if a in self.seen:
                continue
            if not self.dfs(a, set()):
                return False
        return True
                    