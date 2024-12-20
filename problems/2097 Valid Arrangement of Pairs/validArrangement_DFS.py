# DFS, time limit exceeded

from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = []
        self.next = []
    def __repr__(self):
        return str(self.val)

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
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
        
        # DFS
        stack = [(root, [])]    # stack element is (node, [path])
        while stack:
            print(stack)
            input('pause')
            curr, curr_history = stack.pop()
            for node in node_dict[curr.val].next:
                if [curr.val, node.val] not in curr_history:
                    node_history = list(curr_history)
                    node_history.append([curr.val, node.val])
                    stack.append((node, node_history))
                    if len(node_history) == len(pairs):
                        return node_history
        
sol = Solution()
# print(sol.validArrangement([[5,1],[4,5],[11,9],[9,4]]))
# print(sol.validArrangement([[1,3],[3,2],[2,7],[2,6],[6,2]]))
# print(sol.validArrangement([[1,3],[3,2],[2,1]]))
# print(sol.validArrangement([[5,13],[10,6],[11,3],[15,19],[16,19],[1,10],[19,11],[4,16],[19,9],[5,11],[5,6],[13,5],[13,9],[9,15],[11,16],[6,9],[9,13],[3,1],[16,5],[6,5]]))
# print(sol.validArrangement([[874,518],[649,247],[621,559],[774,166],[241,168],[835,421],[168,835],[835,399],[741,436],[958,526],[166,578],[734,812],[436,297],[813,774],[166,559],[518,548],[882,719],[559,741],[819,621],[720,168],[964,187],[518,781],[166,781],[781,436],[719,958],[342,241],[659,392],[27,513],[812,468],[513,910],[187,848],[510,741],[835,392],[813,559],[392,848],[964,813],[241,958],[958,436],[854,241],[813,719],[781,421],[421,649],[720,910],[510,297],[725,835],[848,271],[483,578],[848,336],[854,592],[559,720],[436,399],[297,958],[592,483],[526,734],[854,813],[40,720],[719,510],[548,964],[910,882],[342,854],[578,518],[399,514],[514,813],[22,854],[399,342],[336,297],[392,271],[813,835],[27,166],[436,725],[271,854],[468,659],[421,166],[168,548],[297,526],[271,964],[741,725],[548,27],[910,510],[559,27],[73,40],[526,510],[247,819],[725,874],[578,342],[297,22],[510,813]]))
print(sol.validArrangement([[229,699],[489,928],[92,398],[457,398],[798,838],[75,547],[856,141],[838,141],[356,578],[819,537],[229,458],[229,838],[473,175],[545,826],[705,75],[132,262],[92,974],[141,547],[856,92],[229,856],[838,826],[798,15],[892,157],[578,229],[458,905],[141,856],[157,458],[157,489],[92,458],[838,699],[905,458],[547,798],[928,157],[974,15],[545,132],[545,15],[141,132],[458,175],[856,586],[175,705],[547,229],[928,771],[157,671],[175,473],[132,229],[838,671],[458,356],[262,838],[75,262],[92,798],[156,671],[356,124],[547,175],[262,457],[705,545],[671,156],[928,671],[578,892],[483,856],[586,141],[141,838],[974,928],[356,157],[398,586],[15,157],[905,175],[856,157],[157,856],[398,771],[892,586],[974,473],[262,458],[175,141],[458,92],[175,856],[905,974],[928,229],[826,699],[826,483],[826,905],[905,838],[928,356],[974,905],[124,356],[124,537],[771,545],[262,771],[157,928],[229,157],[547,141],[928,75],[262,974],[856,798],[92,132],[15,141],[141,819],[458,15],[141,905],[458,928],[537,586],[92,819],[473,262],[578,473],[141,458],[15,856],[132,798],[537,974],[586,398],[928,141],[141,262],[771,141],[458,974],[157,771],[398,175],[838,974],[826,92],[175,892],[974,157],[838,356],[699,229],[356,489],[15,771],[771,905],[586,92],[771,92],[798,826],[92,537],[699,458],[671,928],[771,928],[398,928],[699,157],[458,157],[537,905],[974,578],[671,92],[671,75],[157,75],[156,838],[473,398],[928,705],[15,458],[705,458],[157,15],[819,124],[157,92],[699,928],[905,699],[798,262],[458,547],[586,856],[974,489],[856,545],[75,974],[75,578],[905,826],[856,705],[489,547]]))

