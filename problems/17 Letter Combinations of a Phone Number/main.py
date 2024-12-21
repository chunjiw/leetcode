from typing import List

class Solution:

    def grow(self, digits, combination, result):
        pad = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        m = len(combination)
        if m >= len(digits):
            result.append(combination)
            return
        for letter in pad[digits[m]]:
            self.grow(digits, combination + letter, result)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combination = ""
        result = []
        self.grow(digits, combination, result)
        return result

sol = Solution()
print(sol.letterCombinations("23"))