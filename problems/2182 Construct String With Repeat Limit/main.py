from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        src = sorted(cnt.keys())
        lis = []
        while src:
            letter = src[-1]
            if cnt[letter] <= repeatLimit:
                lis.extend([letter] * cnt[letter])
                src.pop()
                # cnt.remove(letter)
            else:
                lis.extend([letter] * repeatLimit)
                cnt[letter] -= repeatLimit
                if len(src) > 1:
                    lis.append(src[-2])
                    cnt[src[-2]] -= 1
                    if cnt[src[-2]] == 0:
                        src.remove(src[-2])
                else:
                    break
        return ''.join(lis)
