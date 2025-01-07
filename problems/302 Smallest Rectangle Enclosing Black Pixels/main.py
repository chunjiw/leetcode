from typing import List

class Solution:

    def rowBlack(self, image, x):
        return any([p == '1' for p in image[x]])

    def colBlack(self, image, y):
        return any([image[x][y] == '1' for x in range(len(image))])
    
    def first(self, image, i, j, fun, TF):
        """
        search for the first m such that f(image, m) is TF (True or False)
        """
        while i < j:
            m = i + (j - i) // 2
            if fun(image, m) == TF:
                j = m
            else:
                i = m + 1
        return i

    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        # from 0 to x, search for first black row which must exist
        top = self.first(image, 0, x, self.rowBlack, True)
        # from x to len(image), search for first white row
        if self.rowBlack(image, len(image)-1):
            bottom = len(image)
        else:
            bottom = self.first(image, x, len(image) - 1, self.rowBlack, False)
        # from 0 to y, search for first black col which must exist
        left = self.first(image, 0, y, self.colBlack, True)
        # from y to len(image[0]), search for first white col
        if self.colBlack(image, len(image[0])-1):
            right = len(image[0])
        else:
            right = self.first(image, y, len(image[0]) - 1, self.colBlack, False)
        return (right - left) * (bottom - top)
