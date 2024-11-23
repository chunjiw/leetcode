class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        val = dict()
        val['I'] = 1
        val['V'] = 5
        val['X'] = 10
        val['L'] = 50
        val['C'] = 100
        val['D'] = 500
        val['M'] = 1000
        syms = list(s)
        prev = val[syms[0]]
        res = prev
        for sym in list(s)[1:]:
            curr = val[sym]
            if prev < curr:
                res -= prev + prev
            res += curr
            prev = curr
        return res