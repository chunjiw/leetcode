class Solution:

    def build(self, candidates, index, target, result, results):
        if target == 0:
            results.append(result.copy())
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                return
            result.append(candidates[i])
            self.build(candidates, i, target - candidates[i], result, results)
            result.pop()
                
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        self.build(candidates, 0, target, [], results)
        return results
