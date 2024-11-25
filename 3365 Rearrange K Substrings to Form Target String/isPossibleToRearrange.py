class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        sl = list(s)
        tl = list(t)
        n = len(sl)
        p = n // k
        count = dict()
        for i in range(k):
            sub = ''.join(sl[p*i : p*i+p])
            if sub not in count:
                count[sub] = 1
            else:
                count[sub] += 1
        for i in range(k):
            sub = ''.join(tl[p*i : p*i+p])
            if sub not in count:
                return False
            else:
                count[sub] -= 1
                if count[sub] < 0:
                    return False
        return True