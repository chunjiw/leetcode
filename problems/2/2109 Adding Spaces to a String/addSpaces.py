class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        strlist = list(s) + [' '] * len(spaces)
        i = len(s) - 1
        j = len(strlist) - 1    # at index j, strlist[j] still needs to be assigned
        k = len(spaces) - 1
        while j >= 0:
            strlist[j] = strlist[i]
            if i == spaces[k]:
                k -= 1
                j -= 1
                strlist[j] = ' '
            i, j = i-1, j-1
        return ''.join(strlist)

