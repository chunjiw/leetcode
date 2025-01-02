class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        self.vowels = {'a', 'e', 'i', 'o', 'u'}
        cumsum = [0] * (len(words) + 1)
        for i, word in enumerate(words):
            cumsum[i] = cumsum[i-1] + (1 if word[0] in self.vowels and word[-1] in self.vowels else 0)
        result = []
        for i, j in queries:
            result.append(cumsum[j] - cumsum[i-1])
        return result