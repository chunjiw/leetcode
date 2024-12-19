from typing import List

from collections import deque

class Solution:

    def mutate(self, a):
        result = []
        for b in 'ACGT':
            if b != a:
                result.append(b)
        return result

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        valid = set(bank)
        if endGene not in valid:
            return -1
        seen = set([startGene])
        queue = deque([startGene])
        steps = 0
        while queue:
            print(queue)
            steps += 1
            for _ in range(len(queue)):
                gene = queue.popleft()
                for i in range(len(gene)):
                    for m in self.mutate(gene[i]):
                        mutationList = list(gene)
                        mutationList[i] = m
                        mutation = ''.join(mutationList)
                        if mutation == endGene:
                            return steps
                        if mutation in seen:
                            continue
                        if mutation in valid:
                            queue.append(mutation)
                            seen.add(mutation)
        return -1

sol = Solution()
result = sol.minMutation("AAAACCCC", "CCCCCCCC", ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"])
print(result)