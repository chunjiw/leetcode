from typing import List

class Solution:

    def justifyLine(self, words, maxWidth):
        n = len(words) - 1
        if n == 0:
            return words[0] + ' ' * (maxWidth - len(words[0]))
        extra = maxWidth - sum([len(word) for word in words])
        for i in range(n):
            words[i] += ' ' * (extra // n)
        i = 0
        extra %= n
        while extra > 0:
            words[i] += ' '
            i += 1
            extra -= 1
        return ''.join(words)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = [words[0]]
        i = 1
        result = []
        while i < len(words):
            curr_len = sum([len(word) for word in line]) + len(line) - 1
            if curr_len + 1 + len(words[i]) <= maxWidth:
                line.append(words[i])
            else:
                result.append(self.justifyLine(line, maxWidth))
                line = [words[i]]
            i += 1
        line = ' '.join(line)
        line += ' ' * (maxWidth - len(line))
        result.append(line)
        return result

sol = Solution()
print(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(sol.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(sol.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))

        
