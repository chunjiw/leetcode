from heapq import heapify, heappush, heappop

class TaskManager:

    def __init__(self, tasks: list[list[int]]) -> None:
        self.heap = [(-p, -t, u) for u, t, p in tasks]
        heapify(self.heap)
        self.pmap = {t:p for _, t, p in tasks}
        self.umap = {t:u for u, t, _ in tasks}

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.heap, (-priority, -taskId, userId))
        self.pmap[taskId] = priority
        self.umap[taskId] = userId

    def edit(self, taskId: int, newPriority: int) -> None:
        u = self.umap[taskId]
        if self.pmap[taskId] == newPriority:
            return
        self.pmap[taskId] = newPriority
        heappush(self.heap, (-newPriority, -taskId, u))
    
    def rmv(self, taskId: int) -> None:
        self.umap.pop(taskId)
        self.pmap.pop(taskId)

    def execTop(self) -> int:
        h = self.heap
        pm = self.pmap
        um = self.umap
        while h and (-h[0][1] not in pm or pm[-h[0][1]] != -h[0][0] or um[-h[0][1]] != h[0][2]):
            heappop(h)
        if not h:
            return -1
        _, nt, u = heappop(h)
        pm.pop(-nt)
        um.pop(-nt)
        return u
