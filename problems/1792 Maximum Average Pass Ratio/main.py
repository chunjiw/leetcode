class Solution:

    def gain(self, cl):
        m, n = cl[0], cl[1]
        return (n-m) / n / (n+1)

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        classes = sorted(classes, key=lambda x: -self.gain(x))
        print(classes)
        n = len(classes)
        if all([cl[0] == cl[1] for cl in classes]):
            return n
        while extraStudents > 0:
            cl = classes[0]
            cl[0] += 1
            cl[1] += 1
            extraStudents -= 1
            i = 0
            while i < n - 1 and self.gain(classes[i]) < self.gain(classes[i+1]):
                classes[i], classes[i+1] = classes[i+1], classes[i]
                i += 1
        return sum([cl[0] / cl[1] for cl in classes]) / n
