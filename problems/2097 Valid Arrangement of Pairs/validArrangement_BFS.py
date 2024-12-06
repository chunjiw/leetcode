# BFS, time limit exceeded

from typing import List

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = []
        self.next = []
    def __repr__(self):
        return str(self.val)

class Solution:

    def noDuplicates(self, seq):
        s = set()
        valid = True
        for i in range(len(seq) - 1):
            if (seq[i], seq[i+1]) in s:
                return False
            else:
                s.add((seq[i], seq[i+1]))
        return True

    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        nodes = []
        node_dict = dict()
        for i, j in pairs:
            if i not in node_dict:
                node_dict[i] = Node(i)
            if j not in node_dict:
                node_dict[j] = Node(j)
            node_dict[i].next.append(node_dict[j])
            node_dict[j].prev.append(node_dict[i])
        root = node_dict[pairs[0][0]]
        for node in node_dict.values():
            if not node.prev:
                root = node
        
        # BFS to get all arrangement, allowing duplicates
        queue = deque([root])
        queue_history = deque([[root]])
        level = 0
        while level < len(pairs):
            print(len(queue))
            input('pause')
            for _ in range(len(queue)):
                curr = queue.popleft()
                curr_history = queue_history.popleft()
                for node in curr.next:
                    node_history = list(curr_history)
                    node_history.append(node)
                    if self.noDuplicates(node_history):
                        queue.append(node)
                        queue_history.append(node_history)
            level += 1

        # search for valid arrangement
        for seq in queue_history:
            s = set()
            valid = True
            for i in range(len(seq) - 1):
                if (seq[i], seq[i+1]) in s:
                    valid = False
                    break
                else:
                    s.add((seq[i], seq[i+1]))
            if not valid:
                continue
            result = []
            for i in range(len(seq) - 1):
                result.append([seq[i].val, seq[i+1].val])
        return result

sol = Solution()
sol.validArrangement([[5,1],[4,5],[11,9],[9,4]])
# print(sol.validArrangement([[1,3],[3,2],[2,7],[2,6],[6,2]]))
# print(sol.validArrangement([[1,3],[3,2],[2,1]]))
# print(sol.validArrangement([[5,13],[10,6],[11,3],[15,19],[16,19],[1,10],[19,11],[4,16],[19,9],[5,11],[5,6],[13,5],[13,9],[9,15],[11,16],[6,9],[9,13],[3,1],[16,5],[6,5]]))
# print(sol.validArrangement([[874,518],[649,247],[621,559],[774,166],[241,168],[835,421],[168,835],[835,399],[741,436],[958,526],[166,578],[734,812],[436,297],[813,774],[166,559],[518,548],[882,719],[559,741],[819,621],[720,168],[964,187],[518,781],[166,781],[781,436],[719,958],[342,241],[659,392],[27,513],[812,468],[513,910],[187,848],[510,741],[835,392],[813,559],[392,848],[964,813],[241,958],[958,436],[854,241],[813,719],[781,421],[421,649],[720,910],[510,297],[725,835],[848,271],[483,578],[848,336],[854,592],[559,720],[436,399],[297,958],[592,483],[526,734],[854,813],[40,720],[719,510],[548,964],[910,882],[342,854],[578,518],[399,514],[514,813],[22,854],[399,342],[336,297],[392,271],[813,835],[27,166],[436,725],[271,854],[468,659],[421,166],[168,548],[297,526],[271,964],[741,725],[548,27],[910,510],[559,27],[73,40],[526,510],[247,819],[725,874],[578,342],[297,22],[510,813]]))

