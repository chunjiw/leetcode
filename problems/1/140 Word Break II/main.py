class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        
        wordDict = set(wordDict)
        solution = []

        def wb(i, word, result):
            if i == len(s):
                if word == '':
                    solution.append(' '.join(result))
                return
            word += s[i]
            if word in wordDict:
                res = result.copy()
                res.append(word)
                wb(i+1, '', res)
            wb(i+1, word, result)
            
        wb(0, '', [])

        return solution

sol = Solution()
print(sol.wordBreak('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog']))
print(sol.wordBreak('catsandog', ['cat', 'cats', 'and', 'sand', 'dog']))

s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
print(sol.wordBreak(s, wordDict))
