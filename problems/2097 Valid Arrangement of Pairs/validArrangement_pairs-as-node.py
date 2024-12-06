# time limit exceeded

from typing import List

class Node:
    def __init__(self, pair):
        self.start = pair[0]
        self.end = pair[1]
        self.prev = []
        self.next = []
    def __repr__(self):
        return str((self.start, self.end))


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        nodes = []
        for pair in pairs:
            curr = Node(pair)
            for node in nodes:
                if curr.end == node.start:
                    curr.next.append(node)
                    node.prev.append(curr)
                if node.end == curr.start:
                    node.next.append(curr)
                    curr.prev.append(node)
            nodes.append(curr)
        root = None
        for node in nodes:
            if not node.prev:
                root = node
        if not root:
            root = nodes[0]
        
        # BFS
        queue = [root]
        queue_history = [[root]]
        visited = {root}
        while queue:
            print(queue, queue_history)
            curr = queue.pop(0)
            curr_history = queue_history.pop(0)
            for node in curr.next:
                if node in visited:
                    continue
                queue.append(node)
                visited.add(node)
                node_history = list(curr_history)
                node_history.append(node)
                queue_history.append(node_history)
                # if len(node_history) == len(pairs):
                #     print(node_history)

sol = Solution()
sol.validArrangement([[5,1],[4,5],[11,9],[9,4]])
sol.validArrangement([[1,3],[3,2],[2,7],[2,6],[6,2]])

