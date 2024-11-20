# 207. Course Schedule

# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:

# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Note:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses < 2:
            return True
        
        graph = [set() for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].add(b)
        
        checked = set()
        
        for node in range(numCourses):
            visited = set()
            if not self.visit(node, graph, visited, checked):
                return False
        return True
    
    def visit(self, node, graph, visited, checked):
        if node in checked:
            return True
        for child in graph[node]:
            if child in visited:
                return False
            visited.add(child)
            if not self.visit(child, graph, visited, checked):
                return False
            visited.remove(child)
        checked.add(node)
        return True    
        
